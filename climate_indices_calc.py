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
import rdh


## Initializing SST data
ds = xr.open_dataset('/Users/ryanharp/Documents/Mozambique_climate_variability_predictability/cleaned_data/OI_v2/OI_v2_monthly')
sst_monthly = ds.sst.compute()
del ds
ds = xr.open_dataset('/Users/ryanharp/Documents/Mozambique_climate_variability_predictability/cleaned_data/OI_v2/OI_v2_monthly_anom')
sst_anom = ds.sst.compute()
del ds
lat = sst_monthly.lat
lon = sst_monthly.lon
time = sst_monthly.time.compute()


## Calculating Nino3.4 Index
sst_monthly_1981_2010 = sst_monthly.sel(time=slice("1981-09-30", "2010-12-31")) #using 1981-2010 climatology to conform with NOAA standards
sst_monthly_clim_1981_2010 = sst_monthly_1981_2010.groupby('time.month').mean(dim='time')
sst_monthly_anom_from_1981_2010 = sst_monthly.groupby('time.month') - sst_monthly_clim_1981_2010
nino3p4_monthly = sst_monthly_anom_from_1981_2010.sel(lat=slice(-5, 5), lon=slice(190, 240)).mean(dim='lat').mean(dim='lon')
del sst_monthly_1981_2010

nino3p4 = np.array(nino3p4_monthly)
nino3p4_13_month_running_mean = rdh.moving_average(nino3p4, 13)

np.savetxt("nino3p4.csv", nino3p4, delimiter=",")
np.savetxt("nino3p4_13.csv", nino3p4_13_month_running_mean, delimiter=",")


## Calculating SIOD Index
siod_conventional_box_diff = sst_anom.sel(lat=slice(-37, -27), lon=slice(55, 65)).mean(dim='lat').mean(dim='lon') - \
                             sst_anom.sel(lat=slice(-28, -18), lon=slice(90, 100)).mean(dim='lat').mean(dim='lon')
siod_conventional = np.array(siod_conventional_box_diff)

siod_modified_box_diff = sst_anom.sel(lat=slice(-37, -27), lon=slice(75, 85)).mean(dim='lat').mean(dim='lon') - \
   sst_anom.sel(lat=slice(-23, -13), lon=slice(83, 93)).mean(dim='lat').mean(dim='lon')
siod_modified = np.array(siod_modified_box_diff)
siod_modified_13_month_running_mean = rdh.moving_average(siod_modified, 13)

# np.savetxt("siod_conventional.csv", siod_conventional, delimiter=",")
# np.savetxt("siod_modified.csv", siod_modified, delimiter=",")
# np.savetxt("siod_modified_13_month_running_mean.csv", siod_modified_13_month_running_mean, delimiter=",")


fig = plt.figure()
ax = plt.plot(time, siod_monthly, color='r')
plt.show()