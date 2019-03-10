''' This snippet generate points along a line at fixed distance '''

from shapely.geometry import MultiPoint
from shapely.geometry import LineString

dist = 5
line = LineString([(3,4),(10,50),(20,25)])

line_lenght = int(line.length)

points = MultiPoint([line.interpolate(j) for j in range(dist,line_lenght,dist)])
print(points)
    