from Graphics import rectangle,circle
from Graphics.Subgraphics import cuboid,sphere
area=rectangle.area(2,3)
print("Area of rectangle:",area)
perimeter=rectangle.perimeter(3,5)
print("Perimeter of rectangle is:",perimeter)
area=circle.a(2)
print("Area of circle:",area)
perimeter=circle.p(3)
print("Perimeter of circle is:",perimeter)
l=20
w=12
h=5
r=2
print("Area of cuboid:",cuboid.a(l,w,h))
print("Perimeter of cuboid:",cuboid.p(l,w,h))
print("Area of sphere:",sphere.a(r))
print("Perimeter of sphere:",sphere.p(r))
