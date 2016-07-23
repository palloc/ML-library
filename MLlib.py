from math import *

"""
-----------------------
       k-means
-----------------------
"""

#Calculate distance from center
def Calc_distance(data, center, d):
    distance = 0

    #Calc d dimentional
    for i in range(d):
        distance += pow(abs(data[i] - center), 2)
    return sqrt(distance)
    
    
