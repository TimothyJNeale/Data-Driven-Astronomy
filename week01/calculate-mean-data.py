'''
This file reads a file with a list of numbers in a csv file and calculates the mean of the numbers.
'''
import numpy as np
import os

def calc_stats(data_file):
    data = np.loadtxt(data_file, delimiter=',')

    # Calculate the mean and median
    mean = float(np.mean(data).round(1))
    median = float(np.median(data).round(1))

    return (mean, median)

DATA_DIRECTORY = 'week01'
DATA_FILE = 'data0.csv'

# derives data file name
data_file = os.path.join(DATA_DIRECTORY, DATA_FILE)
# Check if the file exists
if not os.path.isfile(data_file):
    print("File does not exist")
    exit()

# import csv
# data = []
# # Read the data from the file
# with open(data_file, 'r') as file:
#     for row in file:
#         data.append(row.strip().split(','))

# # convert the data to floats
# data = np.asarray(data, dtype=float)

# print("data: ",data)

# Or to do this using numpy
data = np.loadtxt('week01/data.csv', delimiter=',')
print("data: ",data)
print("Mean and median of the data: ", calc_stats(data_file))