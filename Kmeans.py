from math import *
import random

"""
-----------------------
       k-means
-----------------------
"""


#Calculate distance from center
def Calc_distance(data, point):
    distance = 0
    #Calc d dimentional
    for i in range(len(data)):
        distance += pow(abs(data[i] - point[i]), 2)
    return sqrt(distance)


#Calculate coordinates of the center 
def Calc_center(clustur, c_num):
    num = int(c_num)
    center_data = [0.0 for i in range(len(clustur[0].data))]
    
    #clustur_data ... K_means_data
    for c_data in clustur:
        if c_data.clustur == num:
            for i in range(len(c_data.data)):
                center_data[i] += c_data.data[i] / len(clustur)
    return center_data


#Update coordinates of the center
def Update_center(center_size, clustur):
    new_center = []
    for i in range(center_size):
        new_center.append(Calc_center(clustur, str(i)))
    return new_center


class K_means_data:
    def __init__(self, data, num):
        self.data = data
        self.clustur = random.randint(1, int(num))

    #Update object clustur number
    def Update_clustur(self, center):
        min = Calc_distance(self.data, center[0])
        self.clustur = 0
        for i in range(1, len(center)):
            if min > Calc_distance(self.data, center[i]):
                min = Calc_distance(self.data, center[i])
                self.clustur = i

    
#readfile
def file_open(file_name, num):
    clustur_data = []
    with open(file_name) as file:
        line = file.readlines()
        for i in line:
            clustur_data.append(K_means_data(map(int, i.split(",")), num))
    return clustur_data
