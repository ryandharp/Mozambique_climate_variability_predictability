"""
This script is created to subset climate data for further processing.

Created 10/2/2020 by Ryan Harp.
"""

## Importing Modules

import xarray as xr



## Initializing CHIRPS data
ds = xr.open_mfdataset('/projects/b1045/CHIRPS/*.nc')
precip = ds.precip

# subsetting daily data by area and converting to monthly data
precip_Southern_Africa_daily = precip.sel(latitude=slice(-40, 0), longitude=slice(5, 55))
precip_Southern_Africa_monthly = precip_Southern_Africa_daily.resample(time='M').sum(dim='time')
precip_Southern_Africa_monthly.to_netcdf('~/Mozambique_climate_variability_predictability/cleaned_data/CHIRPS/CHIRPS_Southern_Africa_monthly')

# getting monthly anomalies
precip_Southern_Africa_monthly_clim = precip_Southern_Africa_monthly.groupby('time.month').mean(dim='time')
precip_Southern_Africa_monthly_anom = precip_Southern_Africa_monthly.groupby('time.month') - precip_Southern_Africa_monthly_clim
precip_Southern_Africa_monthly_anom.to_netcdf('~/Mozambique_climate_variability_predictability/cleaned_data/CHIRPS/CHIRPS_Southern_Africa_monthly_anom')

del ds, precip, precip_Southern_Africa_daily, precip_Southern_Africa_monthly, precip_Southern_Africa_monthly_anom, precip_Southern_Africa_monthly_clim



# Initializing OI_v2 data
ds = xr.open_mfdataset('/projects/b1045/OI_v2/*.nc')
sst_daily = ds.sst

# converting daily data to monthly data
sst_monthly = sst_daily.resample(time='M').mean(dim='time')
sst_monthly.to_netcdf('~/Mozambique_climate_variability_predictability/cleaned_data/OI_v2/OI_v2_monthly')

# getting monthly anomalies
sst_monthly_clim = sst_monthly.groupby('time.month').mean(dim='time')
sst_monthly_anom = sst_monthly.groupby('time.month') - sst_monthly_clim
sst_monthly_anom.to_netcdf('~/Mozambique_climate_variability_predictability/cleaned_data/OI_v2/OI_v2_monthly_anom')

# # calculating nino3.4 for data verification purposes
# sst_monthly_1981_2010 = sst_monthly.sel(time=slice("1981-09-30", "2010-12-31"))
# sst_monthly_clim_1981_2010 = sst_monthly_1981_2010.groupby('time.month').mean(dim='time')
# sst_monthly_anom_nino3p4 = sst_monthly.groupby('time.month') - sst_monthly_clim_1981_2010  # using
# nino3p4_monthly = sst_monthly_anom_nino3p4.sel(lat=slice(-5, 5), lon=slice(190, 240)).mean(dim='lat').mean(dim='lon')

del ds, sst_daily, sst_monthly, sst_monthly_anom, sst_monthly_clim



# Initializing ERA5 surface data
ds = xr.open_dataset('/projects/b1045/ERA5_reanalysis/ERA5.surface.t-td-mslp-u-v.mon.1979-2020.nc')
t_2m_monthly = ds.t2m
td_2m_monthly = ds.d2m
u10_monthly = ds.u10
v10_monthly = ds.v10
mslp_monthly = ds.msl

# limiting to 1979-2019 and subsetting by area
t_2m_monthly_1979_2019 = t_2m_monthly.sel(time=slice("1979-01-01", "2019-12-31")).sel(expver=1)
t_2m_Southern_Africa_monthly = t_2m_monthly_1979_2019.sel(latitude=slice(0, -40), longitude=slice(5, 55))
t_2m_Southern_Africa_monthly.to_netcdf('~/Mozambique_climate_variability_predictability/cleaned_data/ERA5/t_2m_Southern_Africa_monthly')

td_2m_monthly_1979_2019 = td_2m_monthly.sel(time=slice("1979-01-01", "2019-12-31")).sel(expver=1)
td_2m_Southern_Africa_monthly = td_2m_monthly_1979_2019.sel(latitude=slice(0, -40), longitude=slice(5, 55))
td_2m_Southern_Africa_monthly.to_netcdf('~/Mozambique_climate_variability_predictability/cleaned_data/ERA5/td_2m_Southern_Africa_monthly')

u10_monthly_1979_2019 = u10_monthly.sel(time=slice("1979-01-01", "2019-12-31")).sel(expver=1)
u10_Southern_Africa_monthly = u10_monthly_1979_2019.sel(latitude=slice(0, -40), longitude=slice(5, 55))
u10_Southern_Africa_monthly.to_netcdf('~/Mozambique_climate_variability_predictability/cleaned_data/ERA5/u10_Southern_Africa_monthly')

v10_monthly_1979_2019 = v10_monthly.sel(time=slice("1979-01-01", "2019-12-31")).sel(expver=1)
v10_Southern_Africa_monthly = v10_monthly_1979_2019.sel(latitude=slice(0, -40), longitude=slice(5, 55))
v10_Southern_Africa_monthly.to_netcdf('~/Mozambique_climate_variability_predictability/cleaned_data/ERA5/v10_Southern_Africa_monthly')

mslp_monthly_1979_2019 = mslp_monthly.sel(time=slice("1979-01-01", "2019-12-31")).sel(expver=1)
mslp_Southern_Africa_monthly = mslp_monthly_1979_2019.sel(latitude=slice(0, -40), longitude=slice(5, 55))
mslp_Southern_Africa_monthly.to_netcdf('~/Mozambique_climate_variability_predictability/cleaned_data/ERA5/smslp_Southern_Africa_monthly')

del ds, mslp_Southern_Africa_monthly, mslp_monthly, mslp_monthly_1979_2019, t_2m_Southern_Africa_monthly, \
    t_2m_monthly, t_2m_monthly_1979_2019, td_2m_Southern_Africa_monthly, td_2m_monthly, \
    td_2m_monthly_1979_2019, u10_Southern_Africa_monthly, u10_monthly, u10_monthly_1979_2019, \
    v10_Southern_Africa_monthly, v10_monthly, v10_monthly_1979_2019



# Initializing ERA5 850hpa data
ds = xr.open_dataset('/projects/b1045/ERA5_reanalysis/ERA5.850hpa.z-q-u-v.mon.1979-2020.nc')
z_monthly = ds.z
q_monthly = ds.q
u_monthly = ds.u
v_monthly = ds.v

# limiting to 1979-2019 and subsetting by area
z_850_monthly_1979_2019 = z_monthly.sel(time=slice("1979-01-01", "2019-12-31")).sel(expver=1)
z_850_Southern_Africa_monthly = z_850_monthly_1979_2019.sel(latitude=slice(0, -40), longitude=slice(5, 55))
z_850_Southern_Africa_monthly.to_netcdf('~/Mozambique_climate_variability_predictability/cleaned_data/ERA5/z_850_Southern_Africa_monthly')

q_850_monthly_1979_2019 = q_monthly.sel(time=slice("1979-01-01", "2019-12-31")).sel(expver=1)
q_850_Southern_Africa_monthly = q_850_monthly_1979_2019.sel(latitude=slice(0, -40), longitude=slice(5, 55))
q_850_Southern_Africa_monthly.to_netcdf('~/Mozambique_climate_variability_predictability/cleaned_data/ERA5/q_850_Southern_Africa_monthly')

u_850_monthly_1979_2019 = u_monthly.sel(time=slice("1979-01-01", "2019-12-31")).sel(expver=1)
u_850_Southern_Africa_monthly = u_850_monthly_1979_2019.sel(latitude=slice(0, -40), longitude=slice(5, 55))
u_850_Southern_Africa_monthly.to_netcdf('~/Mozambique_climate_variability_predictability/cleaned_data/ERA5/u_850_Southern_Africa_monthly')

v_850_monthly_1979_2019 = v_monthly.sel(time=slice("1979-01-01", "2019-12-31")).sel(expver=1)
v_850_Southern_Africa_monthly = v_850_monthly_1979_2019.sel(latitude=slice(0, -40), longitude=slice(5, 55))
v_850_Southern_Africa_monthly.to_netcdf('~/Mozambique_climate_variability_predictability/cleaned_data/ERA5/v_850_Southern_Africa_monthly')

del q_850_Southern_Africa_monthly, q_850_monthly_1979_2019, q_monthly, u_850_Southern_Africa_monthly, \
    u_850_monthly_1979_2019, u_monthly, v_850_Southern_Africa_monthly, v_850_monthly_1979_2019, v_monthly, \
    z_850_Southern_Africa_monthly, z_850_monthly_1979_2019, z_monthly


# Initializing ERA5 700hpa data
ds = xr.open_dataset('/projects/b1045/ERA5_reanalysis/ERA5.700hpa.z-q-u-v.mon.1979-2020.nc')
z_monthly = ds.z
q_monthly = ds.q
u_monthly = ds.u
v_monthly = ds.v

# limiting to 1979-2019 and subsetting by area
z_700_monthly_1979_2019 = z_monthly.sel(time=slice("1979-01-01", "2019-12-31")).sel(expver=1)
z_700_Southern_Africa_monthly = z_700_monthly_1979_2019.sel(latitude=slice(0, -40), longitude=slice(5, 55))
z_700_Southern_Africa_monthly.to_netcdf('~/Mozambique_climate_variability_predictability/cleaned_data/ERA5/z_700_Southern_Africa_monthly')

q_700_monthly_1979_2019 = q_monthly.sel(time=slice("1979-01-01", "2019-12-31")).sel(expver=1)
q_700_Southern_Africa_monthly = q_700_monthly_1979_2019.sel(latitude=slice(0, -40), longitude=slice(5, 55))
q_700_Southern_Africa_monthly.to_netcdf('~/Mozambique_climate_variability_predictability/cleaned_data/ERA5/q_700_Southern_Africa_monthly')

u_700_monthly_1979_2019 = u_monthly.sel(time=slice("1979-01-01", "2019-12-31")).sel(expver=1)
u_700_Southern_Africa_monthly = u_700_monthly_1979_2019.sel(latitude=slice(0, -40), longitude=slice(5, 55))
u_700_Southern_Africa_monthly.to_netcdf('~/Mozambique_climate_variability_predictability/cleaned_data/ERA5/u_700_Southern_Africa_monthly')

v_700_monthly_1979_2019 = v_monthly.sel(time=slice("1979-01-01", "2019-12-31")).sel(expver=1)
v_700_Southern_Africa_monthly = v_700_monthly_1979_2019.sel(latitude=slice(0, -40), longitude=slice(5, 55))
v_700_Southern_Africa_monthly.to_netcdf('~/Mozambique_climate_variability_predictability/cleaned_data/ERA5/v_700_Southern_Africa_monthly')

del  ds, q_700_Southern_Africa_monthly, q_700_monthly_1979_2019, q_monthly, u_700_Southern_Africa_monthly, \
    u_700_monthly_1979_2019, u_monthly, v_700_Southern_Africa_monthly, v_700_monthly_1979_2019, v_monthly, \
    z_700_Southern_Africa_monthly, z_700_monthly_1979_2019, z_monthly



# Initializing ERA5 500hpa data
ds = xr.open_dataset('/projects/b1045/ERA5_reanalysis/ERA5.500hpa.z-omega.mon.1979-2020.nc')
z_monthly = ds.z
omega_monthly = ds.w

# limiting to 1979-2019 and subsetting by area
z_500_monthly_1979_2019 = z_monthly.sel(time=slice("1979-01-01", "2019-12-31")).sel(expver=1)
z_500_Southern_Africa_monthly = z_500_monthly_1979_2019.sel(latitude=slice(0, -40), longitude=slice(5, 55))
z_500_Southern_Africa_monthly.to_netcdf('~/Mozambique_climate_variability_predictability/cleaned_data/ERA5/z_500_Southern_Africa_monthly')

omega_500_monthly_1979_2019 = omega_monthly.sel(time=slice("1979-01-01", "2019-12-31")).sel(expver=1)
omega_500_Southern_Africa_monthly = omega_500_monthly_1979_2019.sel(latitude=slice(0, -40), longitude=slice(5, 55))
omega_500_Southern_Africa_monthly.to_netcdf('~/Mozambique_climate_variability_predictability/cleaned_data/ERA5/omega_500_Southern_Africa_monthly')

del ds, omega_500_Southern_Africa_monthly, omega_500_monthly_1979_2019, omega_monthly, \
    z_500_Southern_Africa_monthly, z_500_monthly_1979_2019, z_monthly



# Initializing ERA5 300hpa data
ds = xr.open_dataset('/projects/b1045/ERA5_reanalysis/ERA5.300hpa.z.mon.1979-2020.nc')
z_monthly = ds.z

# limiting to 1979-2019 and subsetting by area
z_300_monthly_1979_2019 = z_monthly.sel(time=slice("1979-01-01", "2019-12-31")).sel(expver=1)
z_300_Southern_Africa_monthly = z_300_monthly_1979_2019.sel(latitude=slice(0, -40), longitude=slice(5, 55))
z_300_Southern_Africa_monthly.to_netcdf('~/Mozambique_climate_variability_predictability/cleaned_data/ERA5/z_300_Southern_Africa_monthly')

del ds, z_300_Southern_Africa_monthly, z_300_monthly_1979_2019, z_monthly
