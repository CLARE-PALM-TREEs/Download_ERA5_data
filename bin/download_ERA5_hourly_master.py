"""
script for downloading ERA5 reanalysis data from the Copernicus Climate Data Store

Instructions to install the cdsapi here:
https://confluence.ecmwf.int/display/CKB/How+to+download+ERA5#HowtodownloadERA5-3-DownloadERA5datathroughtheCDSAPI
Example script based on:
https://confluence.ecmwf.int/display/WEBAPI/ERA5+daily+retrieval+efficiency
"""
from datetime import date, timedelta
import os
from os import path
import cdsapi
from calendar import isleap
from bin import variables_list as variables
import iris

c = cdsapi.Client(url='https://cds.climate.copernicus.eu/api/v2', key='169329:302ac45c-4e5d-4430-b620-83cc455a3fa9')


def date_range(start_date, end_date):
    """
    return a generator with a sequence of daily dates
    from start_date to end_date (including start but not
    end)

    >>> start_date=date(2023,1,1)
    >>> end_date=date(2023,1,5)
    >>> a=date_range(start_date, end_date)
    >>> print(list(a))
    [datetime.date(2023, 1, 1), datetime.date(2023, 1, 2), datetime.date(2023, 1, 3), datetime.date(2023, 1, 4)]

    """


    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)


def era5_time_variant_request(year: int, month: int, day: int, target: str, era5_dataset: str,
                              variable_file_format: str, var_name: str, latitude_min, latitude_max,
                              longitude_min, longitude_max) -> None:
    """
    An ERA5 request for reanalysis single level data that varies over time.

    Input args:
    ----------
    * year
        year to request data for
    * month
        month to request data for
    * day
        day to request data for
    * target
        output directory
    * era5_dataset
        name of the ERA5 dataset to return ('ERA5' or 'ERA5-Land')
    * variable_file_format
        'pressure-levels' or 'single-levels'
    * var_name
        requested variable name
    * latitude_min
        float or integer of the southernmost latitude
    * latitude_max
        float or integer of the northernmost latitude
    * longitude_min
        float or integer of the westernmost longitude
    * longitude_max
        float or integer of the easternmost longitude
    """

    c.retrieve(
        f'reanalysis-{era5_dataset}{variable_file_format}',
        {
            'variable': var_name,
            'year': year,
            'month': month,
            'day': day,
            'time': ['00:00', '01:00', '02:00',
                     '03:00', '04:00', '05:00',
                     '06:00', '07:00', '08:00',
                     '09:00', '10:00', '11:00',
                     '12:00', '13:00', '14:00',
                     '15:00', '16:00', '17:00',
                     '18:00', '19:00', '20:00',
                     '21:00', '22:00', '23:00'],
            'pressure_level': ['1', '2', '3',
                               '5', '7', '10',
                               '20', '30', '50',
                               '70', '100', '125',
                               '150', '175', '200',
                               '225', '250', '300',
                               '350', '400', '450',
                               '500', '550', '600',
                               '650', '700', '750',
                               '775', '800', '825',
                               '850', '875', '900',
                               '925', '950', '975',
                               '1000', ],
            'format': 'netcdf',
            'product_type': 'reanalysis',
        },
        target)
    cube = iris.load_cube(target)
    cube = cube.intersection(longitude=(longitude_min, longitude_max), latitude=(latitude_min, latitude_max))
    new_target = f'{target[:-4]}_lat_{latitude_min}_to_{latitude_max}_lon_{longitude_min}_to{longitude_max}.nc'
    iris.save(cube, new_target)
    os.remove(target)

def era5_time_invariant_request(target: str, era5_dataset: str, variable_file_format: str, var_name: str,
                                latitude_min, latitude_max, longitude_min, longitude_max) -> None:
    """
    An ERA5 request for reanalysis single level data that does not
    vary over time.

    Input args:
    ----------
    * target
        output directory
    * era5_dataset
        name of the ERA5 dataset to return ('ERA5' or 'ERA5-Land')
    * variable_file_format
        'pressure-levels' or 'single-levels'
    * var_name
        requested variable name
    * latitude_min
        float or integer of the southernmost latitude
    * latitude_max
        float or integer of the northernmost latitude
    * longitude_min
        float or integer of the westernmost longitude
    * longitude_max
        float or integer of the easternmost longitude
    """

    c.retrieve(
        f'reanalysis-{era5_dataset}{variable_file_format}',
        {
            'variable': var_name,
            'year': '2000',
            'day': '01',
            'time': '00:00',
            'month': '01',
            'format': 'netcdf',
            'product_type': 'reanalysis',
        },
        target)
    cube = iris.load_cube(target)
    cube = cube.intersection(longitude=(longitude_min, longitude_max), latitude=(latitude_min, latitude_max))
    new_target = f'{target[:-4]}_lat_{latitude_min}_to_{latitude_max}_lon_{longitude_min}_to{longitude_max}.nc'
    iris.save(cube, new_target)
    os.remove(target)


def download_data(var_name: str, start_year: int, start_month: int, start_day: int,
                  end_year: int, end_month: int, end_day: int, dataset: str, latitude_min=-90,
                  latitude_max=90, longitude_min=-180, longitude_max=180,
                  output_path='/project/applied/Data/') -> None:
    """
    A function to download ERA5 data using the CDS api

    Input args:
    ----------
    * var_name
        requested variable name
    * start_year
        first year requested
    * end_year
        last year requested
    * start_day
        first day requested
    * dataset
        name of the ERA5 dataset to return ('ERA5' or 'ERA5-Land')
    * latitude_min
        float or integer of the southernmost latitude
    * latitude_max
        float or integer of the northernmost latitude
    * longitude_min
        float or integer of the westernmost longitude
    * longitude_max
        float or integer of the easternmost longitude
    * output_path
        string of the directory to store the downloaded files in
    """

    var_handler = variables.Variables()
    if var_name not in var_handler.var_dic.keys():
        raise ValueError(f'Variable {var_name} is not in list of downloadable variables')

    var_info = var_handler.var_dic[var_name]
    if dataset == 'ERA5':
        era5_dataset = 'era5-'
        era5_dataset_version = var_info.dataset_version
    elif dataset == 'ERA5-Land':
        era5_dataset = 'era5-land'
        era5_dataset_version = ''
    else:
        raise ValueError(f'Dataset name {dataset} not recognised. Must be ERA5 or ERA5-Land')

    start_date = date(start_year, start_month, start_day)
    end_date = date(end_year, end_month, end_day)
    if start_date == end_date:
        raise ValueError(f'Start and end date is equal. Cannot get a range')
    if start_date > end_date:
        raise ValueError(f'Start date cannot be after end date')

    if var_info.time_invariant:
        target_path = f'{output_path}{dataset}/time_invariant/'
        if not path.exists(target_path):
            os.makedirs(target_path, exist_ok=True)
            os.chmod(target_path, 0o777)

        target = f'{target_path}era5_{var_info.name}.nc'
        if path.exists(target):
            print(f"{target} already exists, so will not replace")
            return

        print(f"Downloading {target}")
        era5_time_invariant_request(target, era5_dataset, era5_dataset_version, var_name, latitude_min,
                  latitude_max, longitude_min, longitude_max, output_path)
    else:
        target_path = f'{output_path}{dataset}/hourly/{var_info.name}/'
        if not path.exists(target_path):
            os.makedirs(target_path, exist_ok=True)
            os.chmod(target_path, 0o777)

        for single_date in date_range(start_date, end_date):
            _download_days_data(single_date, target_path, era5_dataset, era5_dataset_version, var_info, latitude_min,
                                latitude_max, longitude_min, longitude_max)


def _download_days_data(single_date: date, target_path: str, era5_dataset: str, variable_file_format: str,
                        var_info: variables.VariablesInfo, latitude_min, latitude_max, longitude_min,
                        longitude_max) -> None:
    """
    An internal function to download the hourly data for the requested day

    Input args:
    ----------
    * year
        year to request data for
    * month
        month to request data for
    * day
        day to request data for
    * target_path
        output path for the requested data
    * era5_dataset
        name of the ERA5 data requested
    * variable_file_format
        version of the ERA5 dataset requested
    * var_info
        VariablesInfo object for the variable to request data for
    * latitude_min
        float or integer of the southernmost latitude
    * latitude_max
        float or integer of the northernmost latitude
    * longitude_min
        float or integer of the westernmost longitude
    * longitude_max
        float or integer of the easternmost longitude
    """

    timestamp = '%04d%02d%02d' % (single_date.year, single_date.month, single_date.day)
    target = f'{target_path}era5_hourly_{var_info.name}_{timestamp}.nc'
    if path.exists(target):
        print(f"{target} already exists, so will not replace")
        return

    print(f"downloading {target}")
    if era5_dataset == 'era5-':
        if single_date.year < 1959:
            variable_file_format = f'{variable_file_format}-preliminary-back-extension'

    era5_time_variant_request(single_date.year, single_date.month, single_date.day, target, era5_dataset,
                              variable_file_format, var_info.name, latitude_min, latitude_max, longitude_min,
                              longitude_max)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
