import pandas as pd
import numpy as np
from compiler.ast import flatten

'''
ncols = 178
nrows = 139
xllcorner = 111.875
yllcorner = -44.625
cellsize = 0.25
NODATA_value = -9999
df = pd.read_csv('E:/Userdata/yuy/OneDrive_ANU/Fire/seasgrpb/seasrain.csv')
df = pd.DataFrame(np.array(df))
df.to_csv('E:/Userdata/yuy/OneDrive_ANU/Fire/seasgrpb/rain_zone.csv')
print(df)
'''

for i in range(0, 178):
    col = 'col' + str(i)
    df = pd.read_csv('E:/Userdata/yuy/OneDrive_ANU/Fire/seasgrpb/seasrain.csv', usecols=[col])
    x_coordinate = 111.875 + 0.25*i
    y_coordinate = pd.read_excel('E:/Userdata/yuy/OneDrive_ANU/Fire/seasgrpb/y_coordinate.xlsx', sheet_name='Sheet1', usecols=['y_coordinate'])
    df['x_coordinate'] = x_coordinate
    df['y_coordinate'] = y_coordinate
    print(df)
    df.to_csv('E:/Userdata/yuy/OneDrive_ANU/Fire/seasgrpb/geo_loc.csv', mode='a', header=False)