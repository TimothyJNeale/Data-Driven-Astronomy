'''
A function find_closest that takes a catalogue and the position of a target source (a right ascension 
and declination) and finds the closest match for the target source in the catalogue. 

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
    data = np.loadtxt('week02/bss320.dat', usecols=range(1, 7))
    res = []
    for i in range(len(data)):
        ra1 = hms2dec(data[i][0], data[i][1], data[i][2])
        dec1 = dms2dec(data[i][3], data[i][4], data[i][5])
        res.append((i+1, ra1, dec1))

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

def find_closest(cat, ra, dec):
    
    # Find the closest object
    min_dist = np.inf
    min_id = None

    for id1, ra1, dec1 in cat:

        dist = angular_dist(ra1, dec1, ra, dec)
        if dist < min_dist:
            best_id = id1
            min_dist = dist
            
    return best_id, min_dist

cat = import_bss()
print(find_closest(cat, 175.3, -32.5))
print(find_closest(cat, 32.2, 40.7))