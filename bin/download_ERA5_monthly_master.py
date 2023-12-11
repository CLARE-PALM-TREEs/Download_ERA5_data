import os
from os import path
import cdsapi
import variables_list as variables
from datetime import date

c = cdsapi.Client(url='https://cds.climate.copernicus.eu/api/v2', key='169329:302ac45c-4e5d-4430-b620-83cc455a3fa9')


def date_range(start_date, end_date):
    """
    returns a a generator with a sequence of months
    from the first to the last inclusive

    >>> start_date=date(2023,1,1)
    >>> end_date=date(2023,5,1)
    >>> a=date_range(start_date, end_date)
    >>> print(list(a))
    [datetime.date(2023, 1, 1), datetime.date(2023, 2, 1), datetime.date(2023, 3, 1), datetime.date(2023, 4, 1)]
    """

    new_date = start_date
    while new_date != end_date:
        yield new_date
        new_month = new_date.month + 1
        if new_month < 13:
            new_date = new_date.replace(month=new_month)
        else:
            new_date = new_date.replace(year=new_date.year + 1, month=1)


def download_data(var_name: str, start_year: int, start_month: int,
                  end_year: int, end_month: int, dataset: str) -> None:
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

    start_date = date(start_year, start_month, 1)
    end_date = date(end_year, end_month, 1)
    if start_date == end_date:
        raise ValueError(f'Start and end date are equal. Cannot get a range')

    output_path = '/gws/nopw/j04/palmtrees/reanalysis/'
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
        era5_time_invariant_request(target, era5_dataset, era5_dataset_version, var_name)
    else:
        target_path = f'{output_path}{dataset}/monthly/{var_info.name}/'
        if not path.exists(target_path):
            os.makedirs(target_path, exist_ok=True)
            os.chmod(target_path, 0o777)

        for single_date in date_range(start_date, end_date):
            _download_months_data(single_date, target_path, era5_dataset, era5_dataset_version, var_info)


def era5_time_variant_request(year: int, month: int, target: str, era5_dataset: str, variable_file_format: str,
                              var_name: str) -> None:
    c.retrieve(
        f'reanalysis-{era5_dataset}{variable_file_format}-monthly-means',
        {
            'format': 'netcdf',
            'product_type': 'monthly_averaged_reanalysis',
            'variable': var_name,
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
            'year': year,
            'month': month,
            'time': '00:00',
        },
        target)


def era5_time_invariant_request(target: str, era5_dataset: str, variable_file_format: str, var_name: str) -> None:
    c.retrieve(
        f'reanalysis-{era5_dataset}{variable_file_format}',
        {
            'variable': var_name,
            'year': '2000',
            'time': '00:00',
            'month': '01',
            'format': 'netcdf',
            'product_type': 'monthly_averaged_reanalysis',
        },
        target)


def _download_months_data(single_date: date, target_path: str, era5_dataset: str, variable_file_format: str,
                          var_info: variables.VariablesInfo) -> None:
    timestamp = '%04d%02d' % (single_date.year, single_date.month)
    target = f'{target_path}era5_monthly_{var_info.name}_{timestamp}.nc'
    if path.exists(target):
        print(f"{target} already exists, so will not replace")
        return

    print(f"downloading {target}")
    if era5_dataset == 'era5-':
        if single_date.year < 1959:
            variable_file_format = f'{variable_file_format}-preliminary-back-extension'

    era5_time_variant_request(single_date.year, single_date.month, target, era5_dataset, variable_file_format, var_info.name)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
