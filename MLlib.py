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
    center_data = [0.0 for i in range(len(cluster[0].data))]
    
    #clustur_data ... K_means_data
    for c_data in cluster:
        if c_data.cluster == c_num:
            for i in len(c_data.data):
                center_data[i] += c_data.data[i] / len(c_data)
    return center_data


#Update coordinates of the center
def Update_center(center_size, cluster):
    new_center = []
    for i in range(center_size):
        new_center.append(Calc_center(cluster, i))
    return new_center


class K_means_data:
    def __init__(self, data):
        self.data = data
        self.clustur = random.randint(1,3)

    #Update object cluster number
    def Update_clustur(self, center):
        min = Calc_distance(center[0])
        self.cluster = 0
        for i in range(1, len(center)):
            if min > Calc_distance(center[i]):
                min = Calc_distance(center[i])
                self.cluster = i
    
#readfile
def file_open(file_name):
    clustur_data = []
    with open("file_name") as file:
        line = file.readlines()
        for i in line:
            clustur_data.append(K_means_data(map(int, i.split(","))))
    return clustur_data
