import math
from shapely.geometry import LineString

line = LineString([(-1,0), (0,1)])

p1 = line.coords[0]
p2 = line.coords[-1]

azimuth = math.atan2(p2[0] - p1[0], p2[-1] - p1[-1])
azimuth = math.degrees(azimuth) % 360

print(azimuth)