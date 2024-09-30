'''
This file looks at basic interations with Flexible Image Transport System (FITS) data files.
'''

from astropy.io import fits
import matplotlib.pyplot as plt
import os

DATA_DIRECTORY = 'week01'
DATA_FILE = 'image0.fits'

# derives data file name
data_file = os.path.join(DATA_DIRECTORY, DATA_FILE)
# Check if the file exists
if not os.path.isfile(data_file):
    print("File does not exist")
    exit()

# Open the FITS file
hdulist = fits.open(data_file)
hdulist.info()

data = hdulist[0].data
print(data.shape)

# Plot the 2D array
plt.imshow(data, cmap=plt.cm.viridis)
plt.xlabel('x-pixels (RA)')
plt.ylabel('y-pixels (Dec)')
plt.colorbar()
plt.show()