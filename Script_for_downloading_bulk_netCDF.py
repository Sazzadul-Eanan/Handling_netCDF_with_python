# Import the necessary library

import requests
import numpy as np

# Provide the dataset-archive credentials if the authorization parameter is required

username = ' '
password = ' '     

# Provide the range of the years from the dataset to be downloaded

years = np.arange (1981, 1988)

# Create the loop to access and download the dataset one year after another 

for year in years :
   
    url = 'https://data.chc.ucsb.edu/products/CHIRPS-2.0/global_daily/netcdf/p25/chirps-v2.0.' + str(year) +'.days_p25.nc'
    
    r = requests.get(url, authorization = (username, password), allow_redirects = True)      # Don't use the 'authorization' parameter if the dataset-archive (website) credentials are not required to access    
    
    open (str(year) + '.nc', 'wb').write(r.content)     # Changing the file name as '19xx.nc' while saving