from math import cos, radians, sin
from CarnageEngine.Vector import Vector


class Transform:
    def __init__(self, position:Vector,anchor:Vector, angle=Vector(0,0,0), scale=Vector(1,1,1)) -> None:
        self.position = position
        self.angle = angle
        self.angleInRadians = Vector(radians(self.angle.x), radians(self.angle.y), radians(self.angle.z))
        self.scale = scale
        self.anchor = anchor

        rotationMatrix = Transform.rotationMatrix(self.position-self.anchor, self.angleInRadians)
        # calculates the relative rotation of the position according to the anchor 
        self.transform = ((rotationMatrix) + self.anchor)
        # the final position 

    @property
    def multiViewProjection(self):
        """Returns a Multi View Projection of the vector
        https://en.wikipedia.org/wiki/Multiview_orthographic_projection"""
        return (self.transform.x, self.transform.z)
        

    @staticmethod
    def mulMatrix(i:Vector, a:Vector, b:Vector, c:Vector):
        """Does a multiplication matrix calculation"""
        x = (i.x * a.x) + (i.x * b.x) + (i.x * c.x)
        y = (i.y * a.y) + (i.y * b.y) + (i.y * c.y)
        z = (i.z * a.z) + (i.z * b.z) + (i.z * c.z)
        return Vector(x,y,z)

    @staticmethod
    def rotationMatrix(positionVector:Vector, angleVector:Vector):
        """Calculates the rotation of the vector. 
        https://en.wikipedia.org/wiki/Rotation_matrix#Basic_rotations"""
        xMatrixA = Vector(1,0,0)
        xMatrixB = Vector(0,cos(angleVector.x),-sin(angleVector.x))
        xMatrixC = Vector(0,sin(angleVector.x), cos(angleVector.x))
        xMatrix = Transform.mulMatrix(positionVector, xMatrixA, xMatrixB, xMatrixC)
        # calculating the matrix with x axis rotation 

        yMatrixA = Vector(cos(angleVector.y), 0, sin(angleVector.y))
        yMatrixB = Vector(0,1,0)
        yMatrixC = Vector(-sin(angleVector.y) , 0 , cos(angleVector.y))
        yMatrix = Transform.mulMatrix(xMatrix, yMatrixA, yMatrixB, yMatrixC)
        # calculating the matrix with y axis rotation 

        zMatrixA = Vector(cos(angleVector.z), -sin(angleVector.z), 0)
        zMatrixB = Vector(sin(angleVector.z),cos(angleVector.z),0)
        zMatrixC = Vector(0,0,1)
        zMatrix = Transform.mulMatrix(yMatrix, zMatrixA, zMatrixB, zMatrixC)
        # calculating the matrix with z axis rotation 

        return zMatrix

    def updatePosition(self, newPosition:Vector):
        return Transform(newPosition, self.anchor, self.angle, self.scale)

