''' Find coordinate of Closest Point on Shapely LineString '''

from shapely.geometry import Point
from shapely.geometry import LineString

point = Point(0.0, 0.0)
line = LineString([(-1,0), (0,1)])
dist = line.project(point)
closest_point = line.interpolate(dist)

print(closest_point)