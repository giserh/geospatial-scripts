''' Find coordinate of Closest Point on Shapely Polygon '''

from shapely.geometry import Point
from shapely.geometry import Polygon
from shapely.geometry import LinearRing

point = Point(0.0, 0.0)
poly = Polygon ([(-1 ,1), (2,1), (2,2),(-1,2)])

# Polygon exterior ring
exterior = LinearRing(poly.exterior.coords)

dist = exterior.project(point)
closest_point = exterior.interpolate(dist)

print(closest_point)