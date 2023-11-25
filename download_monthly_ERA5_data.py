'''
--------------------------------------------------------------------------------------------------------
Author: Catherine Bradshaw
Language: Python 3
Created: 30/11/2022
--------------------------------------------------------------------------------------------------------

code to download hourly global ERA5 data to the /project/applied/Data/ERA5/hourly directory

Note: You need to have the ERA5_download_processing library in your PYTHONPATH, a central copy exists at /project/applied/SharedResources

Instructions
for setting up access through the cdsapi:

    1.
    Create a CDS account from https://confluence.ecmwf.int/display/CKB/How+to+download+ERA5

    2.
    Follow the instructions for setting up conda if you have not already done so
    (see https://metoffice.sharepoint.com/sites/TechnologyCommsSite/SitePages/Tooling/Artifactory/Authenticating-Conda-with-Artifactory.aspx
    and Conda for Scientists.pptx
    or Conda for Scientists.pptx)

    3.
    Enter into a terminal window in your homespace the command:
    > conda create --name cds_download --file cds_download.lock

    4. To run code when set up from the terminal:
    > conda activate cds_download
    > python get_ERA5_using_conda.py

HISTORY:

30/11/2022 (CB) - original
'''
import sys
import os
# ensure we have the bin directory on the Python path
sys.path.append(os.getcwd() + '/bin')
from bin import download_ERA5_monthly_master



# dataset (ERA5 or ERA5-Land)
dataset = 'ERA5-Land'

# Note that 1/1/1950 starts at 7am so does not have full hours
# Start date is inclusive
start_year = 2023
start_month = 1

# End date is exclusive
end_year = 2023
end_month = 3

# Commonly requested variables (full list available below)
# 'sea_surface_temperature'
# 'mean_sea_level_pressure'
# '2m_temperature'
# '2m_dewpoint_temperature'
# 'total_precipitation'

var_name = '2m_temperature'

download_ERA5_monthly_master.download_data(var_name, start_year, start_month, end_year, end_month, dataset)

# FULL LIST OF VARIABLES
#
# 'lake_cover',
# 'lake_depth',
# 'low_vegetation_cover',
# 'high_vegetation_cover',
# 'type_of_low_vegetation',
# 'type_of_high_vegetation',
# 'soil_type',
# 'standard_deviation_of_filtered_subgrid_orography',
# 'geopotential',
# 'standard_deviation_of_orography',
# 'anisotropy_of_sub_gridscale_orography',
# 'angle_of_sub_gridscale_orography',
# 'slope_of_sub_gridscale_orography',
# 'land_sea_mask'
# 'convective_inhibition',
# 'friction_velocity',
# 'lake_mix_layer_temperature',
# 'lake_mix_layer_depth',
# 'lake_bottom_temperature',
# 'lake_total_layer_temperature',
# 'lake_shape_factor',
# 'lake_ice_temperature',
# 'lake_ice_depth',
# 'uv_visible_albedo_for_direct_radiation',
# 'minimum_vertical_gradient_of_refractivity_inside_trapping_layer',
# 'uv_visible_albedo_for_diffuse_radiation',
# 'mean_vertical_gradient_of_refractivity_inside_trapping_layer',
# 'near_ir_albedo_for_direct_radiation',
# 'duct_base_height',
# 'near_ir_albedo_for_diffuse_radiation',
# 'trapping_layer_base_height',
# 'trapping_layer_top_height',
# 'cloud_base_height',
# 'zero_degree_level',
# 'instantaneous_10m_wind_gust',
# 'sea-ice_cover',
# 'snow_albedo',
# 'snow_density',
# 'sea_surface_temperature',
# 'ice_temperature_layer_1',
# 'ice_temperature_layer_2',
# 'ice_temperature_layer_3',
# 'ice_temperature_layer_4',
# 'volumetric_soil_water_layer_1',
# 'volumetric_soil_water_layer_2',
# 'volumetric_soil_water_layer_3',
# 'volumetric_soil_water_layer_4',
# 'convective_available_potential_energy',
# 'leaf_area_index_low_vegetation',
# 'leaf_area_index_high_vegetation',
# '10m_u-component_of_neutral_wind',
# '10m_v-component_of_neutral_wind',
# 'surface_pressure',
# 'soil_temperature_level_1',
# 'snow_depth',
# 'charnock',
# 'mean_sea_level_pressure',
# 'boundary_layer_height',
# 'total_cloud_cover',
# '10m_u-component_of_wind',
# '10m_v-component_of_wind',
# '2m_temperature',
# '2m_dewpoint_temperature',
# 'soil_temperature_level_2',
# 'soil_temperature_level_3',
# 'low_cloud_cover',
# 'medium_cloud_cover',
# 'high_cloud_cover',
# 'skin_reservoir_content',
# 'instantaneous_large_scale_surface_precipitation_fraction',
# 'convective_rain_rate',
# 'large_scale_rain_rate',
# 'convective_snowfall_rate_water_equivalent',
# 'large_scale_snowfall_rate_water_equivalent',
# 'instantaneous_eastward_turbulent_surface_stress',
# 'instantaneous_northward_turbulent_surface_stress',
# 'instantaneous_surface_sensible_heat_flux',
# 'instantaneous_moisture_flux',
# 'skin_temperature',
# 'soil_temperature_level_4',
# 'temperature_of_snow_layer',
# 'forecast_albedo',
# 'forecast_surface_roughness',
# 'forecast_logarithm_of_surface_roughness_for_heat',
# '100m_u-component_of_wind',
# '100m_v-component_of_wind',
# 'precipitation_type',
# 'k_index',
# 'total_totals_index'
# 'large_scale_precipitation_fraction',
# 'downward_uv_radiation_at_the_surface',
# 'boundary_layer_dissipation',
# 'surface_sensible_heat_flux',
# 'surface_latent_heat_flux',
# 'surface_solar_radiation_downwards',
# 'surface_thermal_radiation_downwards',
# 'surface_net_solar_radiation',
# 'surface_net_thermal_radiation',
# 'top_net_solar_radiation',
# 'top_net_thermal_radiation',
# 'eastward_turbulent_surface_stress',
# 'northward_turbulent_surface_stress',
# 'eastward_gravity_wave_surface_stress',
# 'northward_gravity_wave_surface_stress',
# 'gravity_wave_dissipation',
# 'top_net_solar_radiation_clear_sky',
# 'top_net_thermal_radiation_clear_sky',
# 'surface_net_solar_radiation_clear_sky',
# 'surface_net_thermal_radiation_clear_sky',
# 'toa_incident_solar_radiation',
# 'vertically_integrated_moisture_divergence',
# 'total_sky_direct_solar_radiation_at_surface',
# 'clear_sky_direct_solar_radiation_at_surface',
# 'surface_solar_radiation_downward_clear_sky',
# 'surface_thermal_radiation_downward_clear_sky',
# 'surface_runoff',
# 'sub_surface_runoff',
# 'snow_evaporation',
# 'snowmelt',
# 'large_scale_precipitation',
# 'convective_precipitation',
# 'snowfall',
# 'evaporation',
# 'runoff',
# 'total_precipitation',
# 'convective_snowfall',
# 'large_scale_snowfall',
# 'potential_evaporation'
# 'mean_surface_runoff_rate',
# 'mean_sub_surface_runoff_rate',
# 'mean_snow_evaporation_rate',
# 'mean_snowmelt_rate',
# 'mean_large_scale_precipitation_fraction',
# 'mean_surface_downward_uv_radiation_flux',
# 'mean_large_scale_precipitation_rate',
# 'mean_convective_precipitation_rate',
# 'mean_snowfall_rate',
# 'mean_boundary_layer_dissipation',
# 'mean_surface_sensible_heat_flux',
# 'mean_surface_latent_heat_flux',
# 'mean_surface_downward_short_wave_radiation_flux',
# 'mean_surface_downward_long_wave_radiation_flux',
# 'mean_surface_net_short_wave_radiation_flux',
# 'mean_surface_net_long_wave_radiation_flux',
# 'mean_top_net_short_wave_radiation_flux',
# 'mean_top_net_long_wave_radiation_flux',
# 'mean_eastward_turbulent_surface_stress',
# 'mean_northward_turbulent_surface_stress',
# 'mean_evaporation_rate',
# 'mean_eastward_gravity_wave_surface_stress',
# 'mean_northward_gravity_wave_surface_stress',
# 'mean_gravity_wave_dissipation',
# 'mean_runoff_rate',
# 'mean_top_net_short_wave_radiation_flux_clear_sky',
# 'mean_top_net_long_wave_radiation_flux_clear_sky',
# 'mean_surface_net_short_wave_radiation_flux_clear_sky',
# 'mean_surface_net_long_wave_radiation_flux_clear_sky',
# 'mean_top_downward_short_wave_radiation_flux',
# 'mean_vertically_integrated_moisture_divergence',
# 'mean_total_precipitation_rate',
# 'mean_convective_snowfall_rate',
# 'mean_large_scale_snowfall_rate',
# 'mean_surface_direct_short_wave_radiation_flux',
# 'mean_surface_direct_short_wave_radiation_flux_clear_sky',
# 'mean_surface_downward_short_wave_radiation_flux_clear_sky',
# 'mean_surface_downward_long_wave_radiation_flux_clear_sky',
# 'mean_potential_evaporation_rate'
# '10m_wind_gust_since_previous_post_processing',
# 'maximum_2m_temperature_since_previous_post_processing',
# 'minimum_2m_temperature_since_previous_post_processing',
# 'maximum_total_precipitation_rate_since_previous_post_processing',
# 'minimum_total_precipitation_rate_since_previous_post_processing'
# 'vertical_integral_of_mass_of_atmosphere',
# 'vertical_integral_of_temperature',
# 'vertical_integral_of_kinetic_energy',
# 'vertical_integral_of_thermal_energy',
# 'vertical_integral_of_potential_and_internal_energy',
# 'vertical_integral_of_potential_internal_and_latent_energy',
# 'vertical_integral_of_total_energy',
# 'vertical_integral_of_energy_conversion',
# 'vertical_integral_of_eastward_mass_flux',
# 'vertical_integral_of_northward_mass_flux',
# 'vertical_integral_of_eastward_kinetic_energy_flux',
# 'vertical_integral_of_northward_kinetic_energy_flux',
# 'vertical_integral_of_eastward_heat_flux',
# 'vertical_integral_of_northward_heat_flux',
# 'vertical_integral_of_eastward_water_vapour_flux',
# 'vertical_integral_of_northward_water_vapour_flux',
# 'vertical_integral_of_eastward_geopotential_flux',
# 'vertical_integral_of_northward_geopotential_flux',
# 'vertical_integral_of_eastward_total_energy_flux',
# 'vertical_integral_of_northward_total_energy_flux',
# 'vertical_integral_of_eastward_ozone_flux',
# 'vertical_integral_of_northward_ozone_flux',
# 'vertical_integral_of_divergence_of_cloud_liquid_water_flux',
# 'vertical_integral_of_divergence_of_cloud_frozen_water_flux',
# 'vertical_integral_of_divergence_of_mass_flux',
# 'vertical_integral_of_divergence_of_kinetic_energy_flux',
# 'vertical_integral_of_divergence_of_thermal_energy_flux',
# 'vertical_integral_of_divergence_of_moisture_flux',
# 'vertical_integral_of_divergence_of_geopotential_flux',
# 'vertical_integral_of_divergence_of_total_energy_flux',
# 'vertical_integral_of_divergence_of_ozone_flux',
# 'vertical_integral_of_eastward_cloud_liquid_water_flux',
# 'vertical_integral_of_northward_cloud_liquid_water_flux',
# 'vertical_integral_of_eastward_cloud_frozen_water_flux',
# 'vertical_integral_of_northward_cloud_frozen_water_flux',
# 'vertical_integral_of_mass_tendency',
# 'total_column_cloud_liquid_water',
# 'total_column_cloud_ice_water',
# 'total_column_supercooled_liquid_water',
# 'total_column_rain_water',
# 'total_column_snow_water',
# 'total_column_water',
# 'total_column_water_vapour',
# 'total_column_ozone'
# 'significant_wave_height_of_first_swell_partition',
# 'mean_wave_direction_of_first_swell_partition',
# 'mean_wave_period_of_first_swell_partition',
# 'significant_wave_height_of_second_swell_partition',
# 'mean_wave_period_of_second_swell_partition',
# 'mean_wave_period_of_second_swell_partition',
# 'significant_wave_height_of_third_swell_partition',
# 'mean_wave_direction_of_third_swell_partition',
# 'mean_wave_period_of_third_swell_partition',
# 'wave_spectral_skewness',
# 'free_convective_velocity_over_the_oceans',
# 'air_density_over_the_oceans',
# 'normalized_energy_flux_into_waves',
# 'normalized_energy_flux_into_ocean',
# 'normalized_stress_into_ocean',
# 'u_component_stokes_drift',
# 'v_component_stokes_drift',
# 'period_corresponding_to_maximum_individual_wave_height',
# 'maximum_individual_wave_height',
# 'model_bathymetry',
# 'mean_wave_period_based_on_first_moment',
# 'mean_zero_crossing_wave_period',
# 'wave_spectral_directional_width',
# 'mean_wave_period_based_on_first_moment_for_wind_waves',
# 'mean_wave_period_based_on_second_moment_for_wind_waves',
# 'wave_spectral_directional_width_for_wind_waves',
# 'mean_wave_period_based_on_first_moment_for_swell',
# 'mean_wave_period_based_on_second_moment_for_wind_waves',
# 'wave_spectral_directional_width_for_swell',
# 'significant_height_of_combined_wind_waves_and_swell',
# 'mean_wave_direction',
# 'peak_wave_period',
# 'mean_wave_period',
# 'coefficient_of_drag_with_waves',
# 'significant_height_of_wind_waves',
# 'mean_direction_of_wind_waves',
# 'mean_period_of_wind_waves',
# 'significant_height_of_total_swell',
# 'mean_direction_of_total_swell',
# 'mean_period_of_total_swell',
# 'mean_square_slope_of_waves',
# 'ocean_surface_stress_equivalent_10m_neutral_wind_speed',
# 'ocean_surface_stress_equivalent_10m_neutral_wind_direction',
# 'wave_spectral_kurtosis',
# 'benjamin_feir_index',
# 'wave_spectral_peakedness'
# 'potential_vorticity',
# 'specific_rain_water_content',
# 'specific_snow_water_content',
# 'geopotential',
# 'temperature',
# 'u_component_of_wind',
# 'v_component_of_wind',
# 'specific_humidity',
# 'vertical_velocity',
# 'vorticity',
# 'divergence',
# 'relative_humidity',
# 'ozone_mass_mixing_ratio',
# 'specific_cloud_liquid_water_content',
# 'specific_cloud_ice_water_content',
# 'fraction_of_cloud_cover'






