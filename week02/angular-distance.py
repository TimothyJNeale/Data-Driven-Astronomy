'''
A function angular_dist that calculates the angular distance between any two points on the 
celestial sphere given their right ascension and declination.

'''
import numpy as np

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

ra1, dec1 = 21.07, 0.1
ra2, dec2 = 21.15, 8.2
print(angular_dist(ra1, dec1, ra2, dec2))

print(angular_dist(10.3, -3, 24.3, -29))

