'''
import_bss 
This function imports the BSS data from the file 'bss.dat' and returns a a list of tuples 
containing the object's ID (an integer) and the coordinates in degrees.

import_super
This function imports the SuperCOSMOS data from the file 'super.csv' and returns a list of tuples 
containing the object's ID (an integer) and the coordinates in degrees.

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

def import_bss():
    data = np.loadtxt('week02/bss.dat', usecols=range(1, 7))
    res = []
    for i in range(len(data)):
        ra1 = hms2dec(data[i][0], data[i][1], data[i][2])
        dec1 = dms2dec(data[i][3], data[i][4], data[i][5])
        res.append((i+1, ra1, dec1))

    return res

def import_super():
    data = np.loadtxt('week02/super.csv', delimiter=',', skiprows=1, usecols=[0, 1, 2])
    res = []
    for i in range(len(data)):
        res.append((i+1, float(data[i][0]), float(data[i][1])))

    return res

print(import_bss())

print(import_super())