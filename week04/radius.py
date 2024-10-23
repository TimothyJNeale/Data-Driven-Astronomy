# Write your query function here
import numpy as np

def query(data_file):
  
  # read in the data from a text file
  data = np.loadtxt(data_file, delimiter=',', usecols=(0, 2))
  data = data[data[:,1]>1,:]
  
  return data


# You can use this to test your code
# Everything inside this if-statement will be ignored by the automarker
if __name__ == '__main__':
  # Compare your function output to the SQL query
  result = query('stars.csv')

  print(result)