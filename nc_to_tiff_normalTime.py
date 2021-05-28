# coding=utf-8
import arcpy
from arcpy.sa import *
arcpy.gp.overwriteOutput = 1

outLoc = r"E:/Userdata/yuy/OneDrive_ANU/Fire/temp_max_day/2019/"  # 输出路径
inNetCDF = r"E:/Userdata/yuy/downloads/climate/temp_max_day_2019.nc"  # 输入路径

variable = 'temp_max_day'  # 此处是.nc数据中的变量名
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
            nowFile = str(dimension_value)
            nowFile = nowFile.replace('/', '_')
            print(nowFile)
            year = nowFile.split('_')[2]
            month = nowFile.split('_')[1]
            day = nowFile.split('_')[0]

            dv1 = ["time", dimension_value]  # 列表
            dimension_values = [dv1]

            outpath = outLoc + 'temp_max_day_' + year + '_' + month + '_' + day + ".tif"
            arcpy.MakeNetCDFRasterLayer_md(inNetCDF, variable, x_dimension, y_dimension, nowFile,
                                           band_dimension, dimension_values, valueSelectionMethod)
            arcpy.CopyRaster_management(nowFile, outpath, "", "", "", "NONE", "NONE", "")
print('success')