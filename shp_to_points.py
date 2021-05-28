import arcpy
arcpy.env.workspace = 'E:/Userdata/yuy/ArcMap_workspace/'

for i in range(2018,2021):
    inFeatures = 'E:/Userdata/yuy/OneDrive_ANU/Fire/FireScar567/FireScar_' + str(i) + '.shp'
    outFeatureClass = 'E:/Userdata/yuy/OneDrive_ANU/Fire/FireScar567/points/FireScar_' \
                      + str(i) + '.shp'
    print(outFeatureClass)

    # Use FeatureToPoint function to find a point inside each park
    arcpy.FeatureToPoint_management(inFeatures, outFeatureClass, "INSIDE")
