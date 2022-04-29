from math import degrees, sqrt
from math import acos

class Vector:
    def __init__(self, x:float, y:float, z:float) -> None:
        self.x = x
        self.y = y
        self.z = z
    
    def vector(self):
        return (self.x, self.y)

    def __add__ (self, other):
        """
        If the given data type is a tuple or Vector, it will add the corresponding values and return one
        If the given data type is integer or float, it will add the given value to all the x y z
        """
        if type(other) == tuple:
            return Vector(self.x + other[0], self.y+other[1], self.z+other[2])
        elif type(other) == int or type(object) == float:
            return Vector(self.x + other, self.y + other, self.z+other)
        elif type(other) == Vector:
            return Vector(self.x + other.x, self.y + other.y, self.z+other.z)
        else:
            raise(f"Operation not supported with vector and {type(other)}")
        # handles addition 

    def __mul__(self, other):
        """
        If the given data type is a tuple or Vector, it will multiply the corresponding values and return one
        If the given data type is integer or float, it will multiply the given value to all the x y z
        """
        if type(other) == tuple:
            return Vector(self.x * other[0], self.y * other[1], self.z * other[2])
        elif type(other) == int or type(object) == float:
            return Vector(self.x * other, self.y * other, self.z * other)
        elif type(other) == Vector:
            return Vector(self.x * other.x, self.y * other.y, self.z *other.z)
        else:
            raise(f"Operation not supported with vector and {type(other)}")
        # handles multiplication 

    def __sub__(self, other):
        """
        If the given data type is a tuple or Vector, it will subtract the corresponding values and return one
        If the given data type is integer or float, it will subtract the given value to all the x y z
        """
        if type(other) == tuple:
            return Vector(self.x - other[0], self.y - other[1], self.z - other[2])
        elif type(other) == int or type(object) == float:
            return Vector(self.x - other, self.y - other, self.z - other)
        elif type(other) == Vector:
            return Vector(self.x - other.x, self.y - other.y, self.z-other.z)
        else:
            raise(f"Operation not supported with Vector and {type(other)}")
        # handles substraction 

    def __truediv__(self, other):
        """
        If the given data type is a tuple or Vector, it will divide the corresponding values and return one
        If the given data type is integer or float, it will divide the given value to all the x y z
        """
        if type(other) == tuple:
            return Vector(self.x / other[0], self.y / other[1], self.z/other[2])
        elif type(other) == int or type(object) == float:
            return Vector(self.x / other, self.y / other, self.z/other)
        elif type(other) == Vector:
            return Vector(self.x / other.x, self.y / other.y, self.z/other.z)
        else:
            raise(f"Operation not supported with Vector and {type(other)}")
        # handles division 

    def __str__(self) -> str:
        """returns a string of the object when needed """
        return str((self.x, self.y, self.z))

    def zero():
        return Vector(0,0,0)

    def dot(self, other):
        """returns the dot product of two vetors"""
        return (self.x*other.x) + (self.y*other.y) + (self.z*other.z)

    def distance(self, other):
        """returns the distance between two vectors"""
        distanceSquare = ((self.x-other.x)*(self.x-other.x)) + ((self.y-other.y)*(self.y-other.y)) + ((self.z-other.z)*(self.z-other.z))
        return sqrt(distanceSquare)

    def angle(self, other):
        """returns the angle between two vectors in angles"""
        dotProduct = self.dot(other)
        numerator = sqrt((self.x*self.x)+ (self.y*self.y)+ (self.z*self.z)) * sqrt((other.x*other.x)+(other.y*other.y) +(other.z*other.z)) 
        try:
            return degrees(acos(dotProduct/numerator) )
        except ZeroDivisionError:
            return 0

