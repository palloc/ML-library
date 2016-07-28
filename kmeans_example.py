import MLlib

cluster_data = []
#readfile
with open("test_data.txt") as file:
    line = file.readlines()
    for i in line:
        cluster_data.append(K_means_data(map(int, i.split(","))))
    
