"""
This script is created to calculate various climate indices from OI_v2 SST data.

Created 10/21/2020 by Ryan Harp.
"""


## Importing Modules

import xarray as xr
import matplotlib.pyplot as plt
import numpy as np
import cartopy as ct
import cartopy.crs as ccrs


## Initializing SST data
ds = xr.open_dataset('/Users/ryanharp/Documents/Mozambique_climate_variability_predictability/cleaned_data/OI_v2/OI_v2_monthly')
sst_monthly = ds.sst.compute()
lat = sst_monthly.lat
lon = sst_monthly.lon


## Calculating Nino3.4 Index
sst_monthly_1981_2010 = sst_monthly.sel(time=slice("1981-09-30", "2010-12-31")) #using 1981-2010 climatology to conform with NOAA standards
sst_monthly_clim_1981_2010 = sst_monthly_1981_2010.groupby('time.month').mean(dim='time')
sst_monthly_anom_from_1981_2010 = sst_monthly.groupby('time.month') - sst_monthly_clim_1981_2010
nino3p4_monthly = sst_monthly_anom_from_1981_2010.sel(lat=slice(-5, 5), lon=slice(190, 240)).mean(dim='lat').mean(dim='lon')
del sst_monthly_1981_2010



