import arcpy
import netCDF4

arcpy.env.workspace = 'E:/Userdata/yuy/ArcMap_workspace/'
inRaster = 'E:/Userdata/yuy/downloads/temp_max_day_2018.tif'
Coordinate_System = "GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]]"
arcpy.DefineProjection_management(inRaster, Coordinate_System)

for i in range(1, 366):
    Index = str(i)
    ncTime = i + 43098
    print(ncTime)
    real_time = netCDF4.num2date(ncTime, units='days since 1900-01-01')
    print(real_time)
    time_value = str(real_time)
    year = time_value.split('-')[0]
    month = time_value.split('-')[1]
    day = time_value.split('-')[2]
    date = day.split(' ')[0]

    outpath = 'E:/Userdata/yuy/OneDrive_ANU/Fire/temp_max_day/2018/temp_max_day_' + year + '_' + month + '_' + date + '.tif'
    print(outpath)
    arcpy.MakeRasterLayer_management(inRaster, Index, "#", "#", Index)
    arcpy.CopyRaster_management(Index, outpath, "", "", "", "NONE", "NONE", "")
