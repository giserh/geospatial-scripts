'''
   p
   °
   ''
   ' '
   '  '      
   px  p1----------p2
   
What if the point p is "outside" the line 
segment p1-p2 and we want to project p on px 
and not to the closest vertex (p1)?

reference: http://geomalgorithms.com/a02-_lines.html
'''

from shapely.geometry import Point
from shapely.geometry import LineString
import numpy as np

point = Point(0.0 ,0.0)
line = LineString([(-1,0.5), (-0.1,0.5)])

v = np.array(line.coords[-1]) - np.array(line.coords[0])
w = np.array(point.coords[0]) - np.array(line.coords[0])
c1 = np.dot(v,w)
c2 = np.dot(v,v)
b = c1/c2
px = np.array(line.coords[0]) + b * v

print(Point(px))