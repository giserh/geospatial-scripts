from osgeo import gdal
src_ds = gdal.Open("INPUT_RASTER")
gt = src_ds.GetGeoTransform()
ulx = gt[0]
uly = gt[3]
lrx = ulx + (src_ds.RasterXSize * gt[1])
lry = uly + (src_ds.RasterYSize * gt[5])

print(ulx,uly,lrx,lry)