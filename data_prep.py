"""
This script is created to subset climate data for further processing.

Created 10/2/2020 by Ryan Harp.
"""

## Importing Modules

import xarray as xr
import matplotlib.pyplot as plt


## Initializing CHIRPS data
ds = xr.open_mfdataset('/projects/b1045/CHIRPS/*.nc')
precip = ds.precip

# subsetting daily data by area and converting to monthly data
precip_Southern_Africa_daily = precip.sel(latitude=slice(-40, 0), longitude=slice(5, 55))
precip_Southern_Africa_monthly = precip_Southern_Africa_daily.resample(time='M').sum(dim='time')
precip_Southern_Africa_monthly.to_netcdf('~/Mozambique_climate_variability_predictability/cleaned_data/CHIRPS_Southern_Africa_monthly')

# getting monthly anomalies
precip_Southern_Africa_monthly_clim = precip_Southern_Africa_monthly.groupby('time.month').mean(dim='time')
precip_Southern_Africa_monthly_anom = precip_Southern_Africa_monthly.groupby('time.month') - precip_Southern_Africa_monthly_clim
precip_Southern_Africa_monthly_anom.to_netcdf('~/Mozambique_climate_variability_predictability/cleaned_data/CHIRPS_Southern_Africa_monthly_anom')

del ds, precip, precip_Southern_Africa_daily, precip_Southern_Africa_monthly, precip_Southern_Africa_monthly_anom, precip_Southern_Africa_monthly_clim


# Initializing OI_v2 data
ds = xr.open_mfdataset('/projects/b1045/OI_v2/*.nc')
sst_daily = ds.sst

# converting daily data to monthly data
sst_monthly = sst_daily.resample(time='M').mean(dim='time')
sst_monthly.to_netcdf('~/Mozambique_climate_variability_predictability/cleaned_data/OI_v2_monthly')

# getting monthly anomalies
sst_monthly_clim = sst_monthly.groupby('time.month').mean(dim='time')
sst_monthly_anom = sst_monthly.groupby('time.month') - sst_monthly_clim
sst_monthly_anom.to_netcdf('~/Mozambique_climate_variability_predictability/cleaned_data/OI_v2_monthly_anom')

# # calculating nino3.4 for data verification purposes
# sst_monthly_1981_2010 = sst_monthly.sel(time=slice("1981-09-30", "2010-12-31"))
# sst_monthly_clim_1981_2010 = sst_monthly_1981_2010.groupby('time.month').mean(dim='time')
# sst_monthly_anom_nino3p4 = sst_monthly.groupby('time.month') - sst_monthly_clim_1981_2010  # using
# nino3p4_monthly = sst_monthly_anom_nino3p4.sel(lat=slice(-5, 5), lon=slice(190, 240)).mean(dim='lat').mean(dim='lon')
