from graphics import rectangle,circle

from graphics.sub_graphics import *

def area_and_perimeter():

    length = int(input("Enter length : "))

    breadth = int(input("Enter breadth : "))

    height = int(input("Enter height : "))

    print(end="\n")

    rectangle.rectangle_fn(length,breadth)

    print(end="\n")

    cuboid.cuboid_fn(length,breadth,height)

    print(end="\n")

    print(end="\n\n")

    radius = int(input("Enter radius : "))

    print(end="\n")

    circle.circle_fn(radius)

    print(end="\n")

    sphere.sphere_fn(radius)


area_and_perimeter()
