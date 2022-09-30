# Import necessary library

from netCDF4 import Dataset
import numpy as np
import pandas as pd

# Reading in the netCDF file

data = Dataset(r'C:\Users\lenovo\Desktop\NetCDF\chirps-1981.nc','r')

# Check the range of the lat long and time data and store them in variables

lat = data.variables['latitude'][:]
lon = data.variables['longitude'][:]
tim = data.variables['time'][:]

# Lat long data of my point of interest (POI) and store them in variables

lat_POI = 23.02109
lon_POI = 91.40152

# Squared difference of lat long data to get the minimum distance between my POI and the nearest embeded point of the netCDF file 

sqr_diff_lat = (lat-lat_POI)**2
sqr_diff_lon = (lon-lon_POI)**2

# Identifying the index of the minimum value for lat and long 

min_index_lat = sqr_diff_lat.argmin()    # This will give us the actual location (within the previously created 'sqr_diff_lat' variable) of the minimum distant value of the latitude at POI
min_index_lon = sqr_diff_lon.argmin()    # This will give us the actual location (within the previously created 'sqr_diff_lon' variable) of the minimum distant value of the longitude at POI

# Displaying the amount of precipitation recieved in the POI on a particular day using the index values of the variables

preci = data.variables['precip']
preipitation_372th_day = preci[6, 292, 1085]    # Corresponding_index_serial = [time, lat, long]

print(preipitation_372th_day)

preipitation_374th_day = preci[8, 292, 1085]   

print(preipitation_374th_day, preci.units)      # Displaying the unit as well

# Taking idea about the date format of the netCDF file using the index for the 'Date' column of my csv to be extracted

date = data.variables['time'].units[11:19]     # To get the idea of the index value of 'time' variable, first run 'data.variables['time'].units' on the console 

print(date)

# Setting the date range variables 

starting_date =  data.variables['time'].units[11:19]
ending_date =  data.variables['time'].units[11:15] + '-12-31'

# Creating the date column 

date_col = pd.date_range(start = starting_date, end = ending_date)

# Creating the model data frame

df = pd.DataFrame(0, columns = ['Precipitation'], index = date_col)

# Creating a numpy array to automatically extract the number of days from the netCDF 'time' variable 

date_time = np.arange(0, data.variables['time'].size)

for time_index in date_time :
    df.iloc[time_index] = preci[time_index, min_index_lat, min_index_lon]

# Saving the time-series into a csv 

df.to_csv('Time-series-at-POI.csv')




