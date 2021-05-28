import arcpy
import csv
import os
from dbfpy import dbf
from arcpy import env
from arcpy.sa import *
arcpy.env.workspace = 'E:/Userdata/yuy/ArcMap_workspace/'
arcpy.CheckOutExtension("Spatial")
arcpy.gp.overwriteOutput = 1

for i in ['SMAP']:
    path = 'E:/Userdata/yuy/downloads/CDFM/SMAP/daily_tiff/'
    inPointFeatures = 'E:/Userdata/yuy/downloads/CDFM/point_template/template_withxy.shp'
    point_path = 'E:/Userdata/yuy/downloads/CDFM/' + str(i) + '/daily_points/'
    out_path = 'E:/Userdata/yuy/downloads/CDFM/' + str(i) + '/daily_values/'

    for raster in os.listdir(path):
        if raster.endswith('.tif'):
            print(raster)
            outPointFeatures = point_path + raster.replace('.tif', '.shp')
            ExtractValuesToPoints(inPointFeatures, (path + raster), outPointFeatures,
                                  "NONE", "VALUE_ONLY")

            print ("Converting %s to csv" % raster)
            point = raster.replace('.tif', '.dbf')
            csv_fn = out_path + raster.replace('.tif', '.csv')
            with open(csv_fn, 'wb') as csvfile:
                in_db = dbf.Dbf(point_path + point)
                out_csv = csv.writer(csvfile)
                names = []
                for field in in_db.header.fields:
                    names.append(field.name)
                out_csv.writerow(names)
                for rec in in_db:
                    out_csv.writerow(rec.fieldData)
                in_db.close()
                print ("Done...")