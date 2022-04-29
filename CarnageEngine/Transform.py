from math import cos, radians, sin
from CarnageEngine.Vector import Vector


class Transform:
    def __init__(self, position:Vector,anchor:Vector, angle=Vector(0,0,0), scale=Vector(1,1,1)) -> None:
        self.position = position
        self.angle = angle
        self.angleInRadians = Vector(radians(self.angle.x), radians(self.angle.y), radians(self.angle.z))
        self.scale = scale
        self.anchor = anchor


        xMatrixA = Vector(1,0,0)
        xMatrixB = Vector(0,cos(self.angleInRadians.x),-sin(self.angleInRadians.x))
        xMatrixC = Vector(0,sin(self.angleInRadians.x), cos(self.angleInRadians.x))
        xMatrix = self.mulMatrix(self.position-self.anchor, xMatrixA, xMatrixB, xMatrixC)
        # calculating the matrix with x axis rotation 

        yMatrixA = Vector(cos(self.angleInRadians.y), 0, sin(self.angleInRadians.y))
        yMatrixB = Vector(0,1,0)
        yMatrixC = Vector(-sin(self.angleInRadians.y) , 0 , cos(self.angleInRadians.y))
        yMatrix = self.mulMatrix(xMatrix, yMatrixA, yMatrixB, yMatrixC)
        # calculating the matrix with y axis rotation 

        zMatrixA = Vector(cos(self.angleInRadians.z), -sin(self.angleInRadians.z), 0)
        zMatrixB = Vector(sin(self.angleInRadians.z),cos(self.angleInRadians.z),0)
        zMatrixC = Vector(0,0,1)
        zMatrix = self.mulMatrix(yMatrix, zMatrixA, zMatrixB, zMatrixC)
        # calculating the matrix with y axis rotation 

        self.transform = ((zMatrix) + self.anchor)

    @property
    def multiViewProjection(self):
        return (self.transform.x, self.transform.z)
        

    
    def mulMatrix(self,i:Vector, a:Vector, b:Vector, c:Vector):
        x = (i.x * a.x) + (i.x * b.x) + (i.x * c.x)
        y = (i.y * a.y) + (i.y * b.y) + (i.y * c.y)
        z = (i.z * a.z) + (i.z * b.z) + (i.z * c.z)
        return Vector(x,y,z)


