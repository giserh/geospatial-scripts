from shapely.geometry import LineString,GeometryCollection

line = LineString([(-1,0), (0,1)])

n_lines = 5

segments = []
for i in range(0,n_lines):
    p1 = line.interpolate((i/float(n_lines)), normalized=True)
    p2 = line.interpolate(((i+1)/float(n_lines)), normalized=True)
    segm = LineString([p1,p2])
    segments.append(segm)
print(GeometryCollection(segments))