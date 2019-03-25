import fiona

# https://download.bbbike.org/osm/bbbike/
shp = fiona.open(r"data\SF_roads_clip.shp","r")

print(len(shp))

xmin,ymin,xmax,ymax = -122.48024451717954,37.68824660040036,-122.47725140033185,37.691319331554254

with fiona.open(r"data\SF_roads_clip.shp","r") as shp:
    shp_filter = shp.filter(bbox=((xmin,ymin,xmax,ymax)))
    for fc in shp_filter:
        print(fc)