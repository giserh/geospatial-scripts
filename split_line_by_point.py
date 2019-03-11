from shapely.geometry import LineString

line = LineString([(-1,0), (0,1)])

point = line.interpolate(0.2, normalized = True)

p1 = line.coords[0]
p2 = line.coords[-1]

# Is point within the line? https://stackoverflow.com/questions/21291725/determine-if-shapely-point-is-within-a-linestring-multilinestring/21295192#21295192
if line.distance(point) < 1e-8:
    print (LineString([p1,point.coords[0]]))
    print (LineString([point.coords[0], p2]))
