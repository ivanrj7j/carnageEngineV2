from math import cos, radians, sin
from CarnageEngine.Vector import Vector


class Transform:
    def __init__(self, position:Vector,anchor=Vector(0,0), angle=Vector(0,0), scale=Vector(1,1)) -> None:
        """
        Handles all the Vector of an object

        :param Vector position: The position of the Object
        :param Vector anchor: The anchor of the Object, all the calculations done are done relative to this position
        :param Vector angle: The angle of the Object, rotation matrix is done based on this parameter
        :param Vector scale: The scale of the Object
        """
        self.position = position
        self.angle = angle
        self.scale = scale
        self.anchor = anchor       

    @property
    def transform(self) -> Vector:
        """
        The Vector with rotation and scale applied to the position of the object
        """
        return self.scalation(self.rotation(self.position, self.angle, self.anchor), self.scale, self.anchor)
        # the final position 

    @staticmethod
    def rotation(position:Vector, angle:Vector, anchor:Vector) -> Vector:
        """
        Calculates the rotation of the vector

        :param Vector position: The position of the Object
        :param Vector angle: The angle(in degrees) of the Object, rotation matrix is done based on this parameter
        :param Vector anchor: The anchor of the Object, all the calculations done are done relative to this position
        """
        angle = angle.inRadians
        x = (cos(angle.x) * position.x) + anchor.x
        if angle.y == 0:
            y=position.y
        else:
            y = (sin(angle.y) * position.y) + anchor.y
        return Vector(x,y)

    @staticmethod 
    def scalation(position:Vector, scale:Vector, anchor:Vector) -> Vector:
        """
        Calculates the scale of the vector

        :param Vector position: The position of the Object
        :param Vector scale: The scale of the Object
        :param Vector anchor: The anchor of the Object, all the calculations done are done relative to this position
        """
        scaleup = Vector(position.x*scale.x, position.y*scale.y)
        return Vector(scaleup.x+anchor.x, scaleup.y+anchor.y)
