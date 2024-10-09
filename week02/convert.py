'''
A function hms2dec that converts right ascension from HMS to decimal degrees'.
Right ascension is always an angle from 0 to 24 hours 

A function dms2dec that converts declination from DMS to decimal degrees.
Declination is always an angle from -90° to +90°.
'''

def hms2dec(hours, minutes, seconds):
    return 15*(hours + minutes/60 + seconds/3600)

def dms2dec(degrees, minutes, seconds):
    if degrees > 0:
        return degrees + minutes/60 + seconds/3600
    else:
        return degrees - minutes/60 - seconds/3600
    

print(hms2dec(23, 12, 6))

print(dms2dec(22, 57, 18))
print(dms2dec(-66, 5, 5.1))

