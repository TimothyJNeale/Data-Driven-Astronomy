'''
This function is the same as median_approx, but it takes a list of FITS filenames and the number of bins.
It returns the median value for each pixels in the image.
'''

import numpy as np
import os
from astropy.io import fits

from medianbinsfits  import median_bins_fits

def median_approx_fits(filenames, B):
    mean, std, left_bin, bins = median_bins_fits(filenames, B)

    dim = mean.shape
    median = np.zeros(dim)
    bin_width = 2 * std / B

    for i in range(dim[0]):
        for j in range(dim[1]):
            total = left_bin[i, j]

            bin_width = 2 * std[i, j] / B
            for b, count in enumerate(bins[i, j]):
                total += count
                if total >= (len(filenames) + 1) / 2:
                    break

            median[i, j] = mean[i, j] - std[i, j] + bin_width * (b + 0.5)

    return median


DATA_DIRECTORY = 'week01'
DATA_FILES = ['image0.fits', 'image1.fits', 'image2.fits']
B = 5
DATA_FILES = ['image0.fits', 'image1.fits', 'image2.fits', 'image3.fits', 'image4.fits', 
              'image5.fits', 'image6.fits', 'image7.fits', 'image8.fits', 'image9.fits', 'image10.fits']
B = 4

# derives data file names
data_files = [os.path.join(DATA_DIRECTORY, fname) for fname in DATA_FILES]

# Check if the files exist
for fname in data_files:
    if not os.path.isfile(fname):
        print("File does not exist:", fname)
        exit()
mean, std, left_bin, bins = median_bins_fits(data_files, B)
print (mean[100,100])
print (std[100,100])
print (left_bin[100,100])
print (bins[100,100])

median = median_approx_fits(data_files, B)
print(median[100,100])



