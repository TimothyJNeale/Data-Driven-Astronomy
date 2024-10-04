'''
The full algorithm for a set of N data points works as follows:

1. Calculate their mean and standard deviation, μ and σ;
2. Set the bounds: minval = μ - σ and maxval = μ + σ. Any value >= maxval is ignored;
3.Set the bin width: width = 2σ /B;
4. Make an ignore bin for counting value < minval;
5. Make B bins for counting values in minval and maxval, e.g. the first bin is minval <= value < minval + width;
6. Count the number of values that fall into each bin;
7. Sum these counts until total >= (N + 1)/2. Remember to start from the ignore bin;
8. Return the midpoint of the bin that exceeded (N + 1)/2.

'''
import numpy as np

def median_bins(values, B):
    '''
    This function takes a list of values and the number of bins, B, and returns the mean μ and standard deviation σ
    of the values, the number of values smaller than μ - σ, the number of values in each bin, and a NumPy array 
    with B elements conaining the bin counts.
    '''

    # Calculate the mean and standard deviation of the values
    mean = float(np.mean(values))
    std = float(np.std(values))

    # Set the bounds
    minval = mean - std
    maxval = mean + std

    # Set the bin width
    width = 2 * std / B

    # Make an ignore bin for counting values < minval
    ignore_bin = 0

    # Make B bins for counting values in minval and maxval  
    bin_counts = np.zeros(B)

    # Count the number of values that fall into each bin
    for value in values:
        if value < minval:
            ignore_bin += 1
        elif value >= maxval:
            continue
        else:
            bin_counts[int((value - minval) // width)] += 1

    return mean, std, ignore_bin, bin_counts


def median_approx(values, B):
    '''
    This function uses median_bins to estimate the median value of a list of values.
    '''
    mean, std, ignore_bin, bin_counts = median_bins(values, B)
    N = len(values)
    width = 2 * std / B
    total = ignore_bin

    for i, count in enumerate(bin_counts):
        total += count
        if total >= (N + 1) / 2:
            break

    return mean - std + width * (i + 0.5)


print(median_bins([1, 1, 3, 2, 2, 6], 3))
print(median_bins([1, 5, 7, 7, 3, 6, 1, 1], 4))

print(median_approx([1, 1, 3, 2, 2, 6], 3))
print(median_approx([1, 5, 7, 7, 3, 6, 1, 1], 4))


print(median_bins([0, 1], 5))
print(median_approx([0, 1], 5))