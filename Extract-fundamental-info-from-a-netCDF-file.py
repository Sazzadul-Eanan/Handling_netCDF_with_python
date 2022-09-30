# Import necessary library

from netCDF4 import Dataset

# Reading in the netCDF file

data = Dataset(r'C:\Users\lenovo\Desktop\NetCDF\CHIRPS-1962.nc','r')     # File source : CHIRPS dataset

# Show the file metadata

print(data)

# Check the file format 

typ = type(data)
print(typ)

# Show all the variables of the file

print(data.variables.keys())

# Show the properties of a specific variable

long = data.variables['longitude']
print(long)

precipitation = data.variables['precip']
print(precipitation)

# Check the dimensions of a specific variable

long_dim = long.dimensions    # To check the dimensions of a variable first extract it as a maky variable such as 'long' in the line 23.
print(long_dim)

precipit_dim = precipitation.dimensions
print(precipit_dim)

# Accessing the data from a specific variable 

time_data = data.variables['time'][:]    # To get all the data under the variable 'time'
print(time_data)

long_data = data.variables['longitude'][:]    
print(long_data)




