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

    #Update object cluster number
    def Update_clustur(self, center):
        max = 0
        
        
#Calculate distance from center
def Calc_distance(data, point):
    distance = 0

    #Calc d dimentional
    for i in range(len(data)):
        distance += pow(abs(data[i] - point[i]), 2)
    return sqrt(distance)




        
