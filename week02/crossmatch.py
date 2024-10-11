'''
A function that crossmatches two catalogues within a maximum distance. It should return a list of 
matches and non-matches for the first catalogue against the second.

The list of matches contains tuples of the first and second catalogue object IDs and their distance. 
The list of non-matches contains the unmatched object IDs from the first catalogue only. Both lists 
should be ordered by the first catalogue's IDs.

The angular distance between two objects is defined as the angle between the two object's positions 
on the celestial sphere.

'''

import numpy as np

# Convert right ascension from HMS to decimal degrees,
def hms2dec(hours, minutes, seconds):
    return 15*float((hours + minutes/60 + seconds/3600))

# Convert declination from DMS to decimal degrees.
def dms2dec(degrees, minutes, seconds):
    if degrees > 0:
        return float(degrees + minutes/60 + seconds/3600)
    else:
        return float(degrees - minutes/60 - seconds/3600)
    
# Input BSS catalogue
def import_bss():
    data = np.loadtxt('week02/bss160.dat', usecols=range(1, 7))
    res = []
    for i in range(len(data)):
        ra1 = hms2dec(data[i][0], data[i][1], data[i][2])
        dec1 = dms2dec(data[i][3], data[i][4], data[i][5])
        res.append((i+1, ra1, dec1))

    return res

def import_super():
    data = np.loadtxt('week02/super360.csv', delimiter=',', skiprows=1, usecols=[0, 1, 2])
    res = []
    for i in range(len(data)):
        res.append((i+1, float(data[i][0]), float(data[i][1])))

    return res

def angular_dist(ra1, dec1, ra2, dec2):
    # Convert to radians
    ra1 = np.radians(ra1)
    dec1 = np.radians(dec1)
    ra2 = np.radians(ra2)
    dec2 = np.radians(dec2)
    
    a = np.sin(np.abs(dec1 - dec2)/2)**2
    b = np.cos(dec1)*np.cos(dec2)*np.sin(np.abs(ra1 - ra2)/2)**2
    d = 2*np.arcsin(np.sqrt(a + b))
    
    return np.degrees(d)


def crossmatch(cat1, cat2, max_radius):
    matches = []
    no_matches = []
    
    for id1, ra1, dec1 in cat1:
        min_dist = np.inf
        min_id = None

        for id2, ra2, dec2 in cat2:
            dist = angular_dist(ra1, dec1, ra2, dec2)
            if dist < min_dist:
                min_id = id2
                min_dist = dist

        if min_dist > max_radius:
            no_matches.append(id1)
        else:
            matches.append((id1, min_id, float(min_dist)))
            
    return matches, no_matches

bss_cat = import_bss()
super_cat = import_super()


max_dist = 40/3600
matches, no_matches = crossmatch(bss_cat, super_cat, max_dist)
print(matches[:3])
print(no_matches[:3])
print(len(no_matches))

max_dist = 5/3600
matches, no_matches = crossmatch(bss_cat, super_cat, max_dist)
print(matches[:3])
print(no_matches[:3])
print(len(no_matches))