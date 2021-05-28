#   Usage: ProjectRaster_management in_raster out_raster out_coor_system {NEAREST | BILINEAR
#                                | CUBIC | MAJORITY} {cell_size} {geographic_transform;
#                                geographic_transform...} {Registration_Point} {in_coor_system}
import arcpy
import os

arcpy.env.workspace = 'E:/Userdata/yuy/ArcMap_workspace/'
arcpy.gp.overwriteOutput = 1

pattern = '_2017'
for i in range(1,2):
    path = 'E:/Userdata/yuy/downloads/CDFM/SMAP/daily_tiff/'
    out = 'E:/Userdata/yuy/downloads/CDFM/SMAP/tiff_wgs84/'
    for raster in os.listdir(path):
        if raster.endswith('.tif') and pattern in raster:
            inRaster = path + raster
            newname = raster.replace('.nc.tif', '.tif')
            # newname = newname.replace('0.05deg', 'reprojected_10km')
            outRaster = out + newname
            print(outRaster)
            prjFile = 'E:/Userdata/yuy/OneDrive_ANU/AUS_boundaries/AUS_adm0.prj'
            arcpy.ProjectRaster_management(inRaster, outRaster, prjFile,
                                           "NEAREST", "0.11946298", "#", "#", "#")