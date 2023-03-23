'''
define two tuples.
Each representing a point in cartesian coordinate(x1,y1) and (x2,y2)
print the distance between the two points
'''
tup1=(int(input("enter the x1 point : ")),int(input("enter the y1 point : ")))
tup2=(int(input("enter the x2 point : ")),int(input("enter the y2 point : ")))
print(((tup2[0]-tup1[0])**2+(tup2[1]-tup1[1])**2)**0.5)
