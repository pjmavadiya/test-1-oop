import sys
from math import pi

class Circle:

    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        r_sq = self.radius * self.radius
        return r_sq * pi
        
    def perimeter(self):
        return 2 * pi * self.radius


if __name__ == "__main__":
    if len(sys.argv) > 1:
        radius = int(sys.argv[1])
        print ("Radius: %d" % radius)
        c1 = Circle(radius)
        print ("Area: %f" % c1.area())
        print ("Perimeter: : %f" % c1.perimeter())
    else:
        c1 = Circle(5)
        print ("Radius: 5")
        print ("Area: %f" % c1.area())
        print ("Perimeter: : %f" % c1.perimeter())
        print("\n\nProvide radius as a command line argument...")