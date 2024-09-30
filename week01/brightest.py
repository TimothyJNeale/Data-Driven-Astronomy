'''
This application is an example of finding the brightest pixel on a FITS image.
'''
from astropy.io import fits
import numpy as np

import os

# The following function finds the brightest pixel in a 2D array from a FITS file
# and returns the inex as a tuple
def brightest(file):
    hdulist = fits.open(file)
    data = hdulist[0].data
    brightest = data.max()
    index = np.where(data == brightest)
    return index

# Find the brightest pixel using argmax function
def brightest_argmax(file):
    hdulist = fits.open(file)
    data = hdulist[0].data
    brightest = data.argmax()
    index = np.unravel_index(brightest, data.shape)
    return index

DATA_DIRECTORY = 'week01'
DATA_FILE = 'image2.fits'

# derives data file name
data_file = os.path.join(DATA_DIRECTORY, DATA_FILE)
# Check if the file exists
if not os.path.isfile(data_file):
    print("File does not exist")
    exit()

print("Brightest pixel index: ", brightest(data_file))
print("Brightest pixel index using argmax: ", brightest_argmax(data_file))

