'''
A funtion to take three arguments: the func function we're timing, the size of the random array to test
and the number of experiments to perform. It should return the average running time for the func function.
'''
import numpy as np
import statistics
import time

def time_stat(func, size, ntrials):
    seconds = []
    for i in range(ntrials):
        # the time to generate the random array should not be included
        data = np.random.rand(size)

        start = time.perf_counter()
        res = func(data)
        elapsed = time.perf_counter() - start

        seconds.append(elapsed)

    # return the average run time
    return np.mean(seconds)  

print('{:.6f}s for statistics.mean'.format(time_stat(statistics.mean, 10**5, 10)))
print('{:.6f}s for np.mean'.format(time_stat(np.mean, 10**5, 1000)))