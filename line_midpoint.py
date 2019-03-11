from shapely.geometry import LineString

line = LineString([(-1,0), (0,1)])
midpoint = line.interpolate(0.5, normalized = True)
print(midpoint)