'''
A functon that takes a list of numbers and returns a tuple of the median and mean of the list (in this order).
'''

def list_stats(values):
    mean = sum(values) / len(values)
    values.sort()
    if len(values) % 2 == 0:
        median = (values[len(values) // 2] + values[len(values) // 2 - 1]) / 2
    else:
        median = values[len(values) // 2]
    return (median, mean)

# Test the function with the following test cases:
data1 = [1.3, 2.4, 20.6, 0.95, 3.1]
data2 = [1.3, 2.4, 20.6, 0.95, 3.1, 2.7]
data3 = [1.5]

print(list_stats(data1))
print(list_stats(data2))
print(list_stats(data3))

