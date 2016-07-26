from math import *

"""
-----------------------
       k-means
-----------------------
"""

class K_means_data:
    def __init__(self, data):
        self.data = data
        clustur = 0

        
#Calculate distance from center
def Calc_distance(data, center, d):
    distance = 0

    #Calc d dimentional
    for i in range(d):
        distance += pow(abs(data[i] - center), 2)
    return sqrt(distance)
    


        
