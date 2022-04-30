from math import cos, radians, sin

from pygame import Rect
import pygame
from CarnageEngine.Transform import Transform
from CarnageEngine.Vector import Vector


class Camera:
    def __init__(self, position=Vector(0,0,0), fov=45, angle=Vector(0,0,0)) -> None:
        self.position = position
        self.fov = fov
        self.angle = angle
        self.angleInRadians = Vector(radians(self.angle.x), radians(self.angle.y), radians(self.angle.z))

    def convertCordinates(self, targetObj:Transform):
        """Does a prespective projection to the object
        https://en.wikipedia.org/wiki/3D_projection#Perspective_projection"""
        rotationMatrix = Transform.rotationMatrix(targetObj.transform-self.position, self.angleInRadians)
        w = rotationMatrix.distance(targetObj.position)
        if self.position.y>rotationMatrix.y:
            w = -w
            # this is experimental 
        # distance between object and camera

        return (rotationMatrix.x, rotationMatrix.z)

    def Update(self, children, window):
        """
        Runs every time the frame is refreshed
        """
        if len(children) > 0:
            for child in children:
                child.Update(window, self)
                for grandChild in child.ChildrenList:
                    if type(grandChild) == Transform:
                        square = Rect(self.convertCordinates(child), (25,25))
                        pygame.draw.rect(window.screen, (0,0,0), square)
