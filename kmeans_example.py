from MLlib import *
import sys
import matplotlib.pyplot as plt

clustur_num = 3
#readfile
clustur_data = file_open(sys.argv[1], clustur_num)

for i in range(100):
    center = Update_center(clustur_num, clustur_data)
    for c in clustur_data:
        c.Update_clustur(center)
    print center

"""
--------------------
     plot data 
--------------------
"""
for i in clustur_data:
    if i.clustur == 1:
        plt.plot(i.data[0], i.data[1],  "ro")
    elif i.clustur == 2:
        plt.plot(i.data[0], i.data[1],  "bo")
    else:
        plt.plot(i.data[0], i.data[1],  "yo")
        
#plt.axis([1111,255255255255,3000000000,700000000])
plt.show()

