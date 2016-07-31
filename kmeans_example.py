from MLlib import *
import sys
clustur_num = 3
#readfile
clustur_data = file_open(sys.argv[1], str(clustur_num))

for i in range(10):
    center = Update_center(clustur_num, clustur_data)
    for c in clustur_data:
        c.Update_clustur(center)
    print center

