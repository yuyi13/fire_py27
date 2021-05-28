import arcpy
import os
from arcpy import env

arcpy.env.workspace = 'E:/Userdata/yuy/ArcMap_workspace/'
arcpy.gp.overwriteOutput = 1

for i in ['AWRA', 'CCI']:
    path = 'E:/Userdata/yuy/downloads/CDFM/' + str(i) + '/final_tiff/'
    out = 'E:/Userdata/yuy/downloads/CDFM/' + str(i) + '/netCDF/'
    for filename in os.listdir(path):
        if filename.endswith('.tif'):
            print(filename)
            inRaster = path + filename
            outNetCDFFile = out + filename.replace('.tif', '.nc')
            variable = 'soil_moisture'
            units = 'meter'
            XDimension = 'coordinate_x'
            YDimension = 'coordinate_y'
            bandDimension = ""
            compressionLevel = ""

            arcpy.RasterToNetCDF_md(inRaster, outNetCDFFile, variable, units,
                                    XDimension, YDimension, bandDimension, compressionLevel)