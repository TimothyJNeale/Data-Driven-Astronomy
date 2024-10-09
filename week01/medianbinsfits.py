'''
This function is the same as median_bins, but it takes a list of FITS filenames and the numbe rof bins.
It returns the mean, std, left_bin, bins of all pixels in the image.

The mean and standared deviation iof the FITS files are calculated using the running_stats function from helper.py.
'''

import numpy as np
import os
from astropy.io import fits

from helper import running_stats

def median_bins_fits(filenames, B):
    '''
    Calculates the median value of a list of FITS files using the median_bins function.
    '''
    mean, std = running_stats(filenames)

    # Find dimensions of the image
    dim = mean.shape

    # Initialise the bins
    left_bin = np.zeros(dim)
    bins = np.zeros((dim[0], dim[1], B))
    bin_width = 2 * std / B

    # Loop over all FITS files
    for filename in filenames:
        hdulist = fits.open(filename)
        data = hdulist[0].data
        hdulist.close()

        # Loop over all pixels
        for i in range(dim[0]):
            for j in range(dim[1]):
                value = data[i, j]
                if value < mean[i, j] - std[i, j]:
                    left_bin[i, j] += 1
                elif value >= mean[i, j] + std[i, j]:
                    continue
                else:
                    bins[i, j, int((value - mean[i, j] + std[i, j]) // bin_width[i, j])] += 1

    return mean, std, left_bin, bins

DATA_DIRECTORY = 'week01'
DATA_FILES = ['image0.fits', 'image1.fits', 'image2.fits']
B = 5
DATA_FILES = ['image0.fits', 'image1.fits', 'image2.fits', 'image3.fits', 'image4.fits', 
              'image5.fits', 'image6.fits', 'image7.fits', 'image8.fits', 'image9.fits', 'image10.fits']
B = 4

# derives data file names
data_files = [os.path.join(DATA_DIRECTORY, file) for file in DATA_FILES]
# Check if the files exist
for file in data_files:
    if not os.path.isfile(file):
        print("File does not exist")
        exit()

mean, std = running_stats(data_files)
#print(mean[100,100], std[100,100])

mean, std, left_bin, bins = median_bins_fits(data_files, B)
print(mean[100,100], std[100,100], left_bin[100,100], bins[100,100])