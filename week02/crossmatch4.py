'''
A function that crossmatches two catalogues within a maximum distance. It should return a list of 
matches and non-matches for the first catalogue against the second.

The list of matches contains tuples of the first and second catalogue object IDs and their distance. 
The list of non-matches contains the unmatched object IDs from the first catalogue only. Both lists 
should be ordered by the first catalogue's IDs.

All conversions to radians are carried out before any crossmatching occures.

The angular distance between two objects is defined as the angle between the two object's positions 
on the celestial sphere.

'''

import numpy as np
import time

# Caalculate the angular distance between two objects with inputs in radians and output in radians
def angular_dist(ra1, dec1, ra2, dec2):
    a = np.sin(np.abs(dec1 - dec2)/2)**2
    b = np.cos(dec1)*np.cos(dec2)*np.sin(np.abs(ra1 - ra2)/2)**2
    
    return 2*np.arcsin(np.sqrt(a + b))


def crossmatch(cat1, cat2, max_radius):
    '''
    Both catalogues are given as an N×2 NumPy array of floats. 
    Each row contains the coordinates of a single object. 
    The two columns are the RA and declination.
    '''
    max_radius = np.radians(max_radius)
    
    # time at the start of the function
    start_time = time.perf_counter()

    matches = []
    no_matches = []

    # convert to radians
    cat1 = np.radians(cat1)
    cat2 = np.radians(cat2)

    for id1, (ra1, dec1) in enumerate(cat1):
        min_id = None

        ra2s = cat2[:, 0]
        dec2s = cat2[:, 1]
        dists = angular_dist(ra1, dec1, ra2s, dec2s)
        min_dist = np.min(dists)
        min_id = np.argmin(dists)

        if min_dist > max_radius:
            no_matches.append(id1)
        else:
            matches.append((id1, int(min_id), float(min_dist)))

    # time at the end of the function
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
            
    return matches, no_matches, elapsed_time


# A function to create a random catalogue of size n
def create_cat(n):
    ras = np.random.uniform(0, 360, size=(n, 1))
    decs = np.random.uniform(-90, 90, size=(n, 1))
    return np.hstack((ras, decs))


ra1, dec1 = np.radians([180, 30])
cat2 = [[180, 32], [55, 10], [302, -44]]
cat2 = np.radians(cat2)
ra2s, dec2s = cat2[:,0], cat2[:,1]
dists = angular_dist(ra1, dec1, ra2s, dec2s)
print(np.degrees(dists))


cat1 = np.array([[180, 30], [45, 10], [300, -45]])
cat2 = np.array([[180, 32], [55, 10], [302, -44]])
matches, no_matches, time_taken = crossmatch(cat1, cat2, 5)
print('matches:', matches)
print('unmatched:', no_matches)
print('time taken:', time_taken)


# # Test your function on random inputs
# np.random.seed(0)
# cat1 = create_cat(1000)
# cat2 = create_cat(1000)
# matches, no_matches, time_taken = crossmatch(cat1, cat2, 5)
# print('matches:', matches)
# print('unmatched:', no_matches)
# print('time taken:', time_taken)