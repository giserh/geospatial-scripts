from shapely.geometry import Point
from shapely.geometry import Polygon

# WGS84 Bounds
coordinates = [-180,-90,180, 90]

LowerLeft = Point(coordinates[0],coordinates[1])
LowerRight = Point(coordinates[2],coordinates[1])
UpperLeft = Point(coordinates[0],coordinates[3])
UpperRight = Point(coordinates[2],coordinates[3])

poly = Polygon([[UpperLeft.x,UpperLeft.y],[UpperRight.x,UpperRight.y],[LowerRight.x,LowerRight.y],[LowerLeft.x,LowerLeft.y]])
print(poly)