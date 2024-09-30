'''
This application reads in a set of csv files which contain a 2D araay of data with the same dimensions. 
The application calculates the mean and returns the results in a numpy array
'''
import numpy as np
import os

DATA_DIRECTORY = 'week01'

def mean_datasets(data_files):
    # initialise the data variable
    data = None
    # Read the data files
    for data_file in data_files:
        data_file = os.path.join(DATA_DIRECTORY, data_file)
        # Check if the file exists
        if not os.path.isfile(data_file):
            print(f"File {data_file} does not exist")
            exit()
        if data is None:
            data = np.loadtxt(data_file, delimiter=',')
        else:
            data += np.loadtxt(data_file, delimiter=',')
        
    # Calculate the mean
    mean = data / len(data_files)
    mean = mean.round(1)

    return mean

print("Mean of the data: ", mean_datasets(['data1.csv', 'data2.csv', 'data3.csv']))



