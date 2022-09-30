# Import the 'glob' module it will help to sort out only the netCDF file from a destination where there is other file formats
# Then store all the netCDF files in the same destination folder of the script you are working on  

import glob
from netCDF4 import Dataset
import pandas as pd
import numpy as np

# Creating an empty python list to store all the years

all_years = []

for file in glob.glob('*.nc') :      # Here the * is given for identifying all the netCDF file
    print(file)
    data = Dataset(file, 'r')
    time = data.variables['time']
    year = time.units[11:15]         # Here the index value is to sort out the year as '19xx' format 
    all_years.append(year)
    
# Creating an empty pandas dataframe covering the whole range of data
    
year_start = min(all_years)
year_end = max(all_years)    

date_range = pd.date_range(start = str(year_start)+'-01-01', 
                           end = str(year_end)+'-12-31', freq = 'D')     # 'D' means daily interval, to get the data in monthly interval input'M' 

df = pd.DataFrame(0, columns = ['Precipitation'], index = date_range)    # 0 is the dummy value for the newly created column 'Precipitation'

# Defining the lat lon for the point of interest (POI)

lat_POI = 27.697817
lon_POI = 85.329806

# Controling the extraction sequence of netCDF file

all_years.sort()     # This will keep the years in ascending order

for yr in all_years :
    # Reading-in the data
    data = Dataset(str(yr) +'.nc', 'r')

    # Storing the lat and lon data of the netCDF file into variables 
    lat = data.variables['latitude'][:]
    lon = data.variables['longitude'][:]
    
    # Squared difference between the specified lat lon and the lat lon of the netCDF file
    sqr_diff_lat = (lat-lat_POI)**2
    sqr_diff_lon = (lon-lon_POI)**2
    
    # Identify the index of the minimum value for lat and lon
    min_lat_index = sqr_diff_lat.argmin()
    min_lon_index = sqr_diff_lon.argmin()
    
    # Accessing the precipitation data 
    precipitation = data.variables['precip']
    
    # Creating date range column for each year during each iteration
    start = str(yr) + '-01-01'
    end = str(yr) + '-12-31'
    d_range = pd.date_range(0, start = start, end = end, freq = 'D')
    
    # Nested 'for loop' to iterate through each individual year using the index value
    for t_index in np.arange(0, len(d_range)) :
        print('Recording the value for : ' +str(d_range[t_index]))       # This will show the real-time recording status on the console
        df.loc[d_range[t_index]]['precipitation'] = precipitation[t_index, min_lat_index, min_lon_index]

df.to_csv('Time-series-at-POI-from-multiple-netCDF-file.csv')










