import os
from shutil import copy

path = "E:/Userdata/yuy/downloads/insitu_comparison/rainfall_testData/rainfall_csv/"

for i in range(1,10):
    for filename in os.listdir(path):
        if filename.endswith('_' + str(i) + '.dbf.csv'):
            print(filename)
            filename1 = filename.replace('_' + str(i) + '.dbf', '_0' + str(i) + '.dbf')
            copy((path + filename), (path + filename1))
            os.remove((path + filename))
print("OK")