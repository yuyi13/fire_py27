import arcpy
import os
import glob
from arcpy import env
from arcpy.sa import *
arcpy.CheckOutExtension("spatial")

raster_path = 'E:/Userdata/yuy/downloads/Fire/temp_max_day/'
output_path = 'E:/Userdata/yuy/downloads/Fire/variables/'
inRaster = glob.glob(os.path.join(raster_path, "*.tif"))
print(inRaster)
out = output_path + 'annual_temp_max.tif'
arcpy.gp.CellStatistics_sa((inRaster), out, "MEAN", "DATA")

print("OK")