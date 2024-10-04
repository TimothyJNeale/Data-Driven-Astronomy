'''
A median_fits function which takes a list of FITS filenames, loads them into a NumPy array, and calculates the 
median image (where each pixel is the median of that pixel over every FITS file).

Your function should return a tuple of the median NumPy array, the time it took the function to run, and the 
amount of memory (in kB) used to store all the FITS files in the NumPy array in memory.

The running time should include loading the FITS files and calculating the median.
'''
from astropy.io import fits
import numpy as np
import time
import os

def median_fits(files):
    start = time.perf_counter()
    data = []
    for file in files:
        hdulist = fits.open(file)
        data.append(hdulist[0].data)

    data = np.array(data)
    median = np.median(data, axis=0)
    elapsed_time = time.perf_counter() - start
    memory = data.nbytes / 1024
    return (median, elapsed_time, memory)

DATA_DIRECTORY = 'week01'
DATA_FILES = ['image0.fits', 'image1.fits']

# derives data file names
data_files = [os.path.join(DATA_DIRECTORY, file) for file in DATA_FILES]
# Check if the files exist
for file in data_files:
    if not os.path.isfile(file):
        print("File does not exist")
        exit()

result = median_fits(data_files)
print(result[0][100,100], result[1], result[2])