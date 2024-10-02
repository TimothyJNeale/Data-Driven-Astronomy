'''
This function function that takes a list of FITS files as an argument, reads them in, and returns 
the mean image data of the FITS files. All the images have the same dimensions and your calculated 
mean array should match those dimensions.
'''

from astropy.io import fits
#import numpy as np

import os

def mean_fits(files):
    # Read the first file
    hdulist = fits.open(files[0])
    data = hdulist[0].data
    hdulist.close()
    # Sum the images
    for file in files[1:]:
        hdulist = fits.open(file)
        data += hdulist[0].data
        hdulist.close()
    # Calculate the mean
    mean = data / len(files)
    return mean

DATA_DIRECTORY = 'week01'
DATA_FILES1 = ['image0.fits', 'image1.fits', 'image2.fits']
DATA_FILES2 = ['image0.fits', 'image1.fits', 'image3.fits']
DATA_FILES3 = ['image0.fits', 'image1.fits', 'image2.fits', 'image3.fits', 'image4.fits']

# derives data file name
data_files = [os.path.join(DATA_DIRECTORY, file) for file in DATA_FILES3]

# Check if the file exists
for file in data_files:
    if not os.path.isfile(file):
        print("File does not exist")
        exit()

print("Mean image data: ", mean_fits(data_files)[100,100])

# The output of the code is:
# Mean image DATA_FILES1:  0.017356586332122486
# Mean image DATA_FILES12  0.01006323037048181
# Mean image DATA_FILES12  0.014150320738554