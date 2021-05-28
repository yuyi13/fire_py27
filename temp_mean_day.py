import arcpy
import os
from arcpy import env
from arcpy.sa import *
arcpy.CheckOutExtension("spatial")

path1 = 'E:/Userdata/yuy/downloads/Fire/temp_max_day/'
path2 = 'E:/Userdata/yuy/downloads/Fire/temp_min_day/'
output_path = 'E:/Userdata/yuy/downloads/Fire/temp_mean_day/'

for raster1 in os.listdir(path1):
    if raster1.endswith('.tif'):
        raster2 = raster1.replace('max', 'min')
        raster3 = raster1.replace('max', 'mean')
        inRaster1 = path1 + raster1
        inRaster2 = path2 + raster2
        out = output_path + raster3
        print(inRaster1, inRaster2)
        arcpy.gp.CellStatistics_sa((inRaster1, inRaster2), out, "MEAN", "DATA")
print("OK")