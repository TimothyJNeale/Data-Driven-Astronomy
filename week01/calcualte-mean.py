# This is a simple example of calculating the mean of a list of numbers
# The mean is the sum of the numbers divided by the number of numbers

import numpy as np

# Define a list of numbers
data = [1, 2.2, 0.3, 3.4, 7.9]

def calculate_mean(data):
    # Calculate the sum of the numbers
    sum = 0
    for num in data:
        sum += num

    # Calculate the mean
    mean = sum / len(data)

    return mean 

# Call the function and print the result
print("Sum of list: ",sum(data))
print ("Length of list: ",len(data))
print("The mean calculated via procedure: ",calculate_mean(data))

'''
Output: 
14.8
5
2.96
'''

print("The mean of the list calculated with numpy is: ", np.mean(data))