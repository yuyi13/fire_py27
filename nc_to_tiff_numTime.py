# coding=utf-8
import arcpy
from arcpy.sa import *
import netCDF4
arcpy.env.workspace = 'E:/Userdata/yuy/ArcMap_workspace/'
arcpy.gp.overwriteOutput = 1

outLoc = r"E:/Userdata/yuy/OneDrive_ANU/Fire/rain_day/"  # 输出路径
inNetCDF = r"E:/Userdata/yuy/downloads/climate/rain_day_2017.nc"  # 输入路径

variable = 'rain_day'  # 此处是.nc数据中的变量名
x_dimension = "longitude"
y_dimension = "latitude"
band_dimension = ""
valueSelectionMethod = "BY_VALUE"  # 以上五个变量为第一个函数会用到的变量，提前定义好

nc_FP = arcpy.NetCDFFileProperties(inNetCDF)  # 读取netCDF文件
nc_Dim = nc_FP.getDimensions()  # 获取维度信息，返回一个维度列表 ['lon','lat','time']

'''
在一个.nc文件中有365个时间，每天有一个降水数据，所以导出有365个tiff图像
为了给导出图像方便命名，要使用 dimension_values ，每一个输出的变量值都是使用该维度的值
'''

for dimension in nc_Dim:
    if dimension == "time":
        length = nc_FP.getDimensionSize(dimension)  # 获取维度的大小
        for i in range(0, length):
            dimension_value = nc_FP.getDimensionValue(dimension, i)  # 遍历每一个时间值
            print(dimension_value)
            real_time = netCDF4.num2date(dimension_value, units='days since 1900-01-01')
            print(real_time)
            nowFile = str(dimension_value)
            time_value = str(real_time)
            year = time_value.split('-')[0]
            month = time_value.split('-')[1]
            day = time_value.split('-')[2]
            day = day.split(' ')[0]

            dimension_values = "time '{}'".format(dimension_value)

            outpath = outLoc + 'rain_day_' + year + '_' + month + '_' + day + ".tif"
            arcpy.MakeNetCDFRasterLayer_md(inNetCDF, variable, x_dimension, y_dimension, nowFile,
                                           band_dimension, dimension_values, valueSelectionMethod)
            arcpy.CopyRaster_management(nowFile, outpath, "", "", "", "NONE", "NONE", "")
print('success')