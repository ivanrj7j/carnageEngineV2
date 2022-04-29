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
        xMatrixA = Vector(1,0,0)
        xMatrixB = Vector(0,cos(self.angleInRadians.x),-sin(self.angleInRadians.x))
        xMatrixC = Vector(0,sin(self.angleInRadians.x), cos(self.angleInRadians.x))
        xMatrix = targetObj.mulMatrix(self.position, xMatrixA, xMatrixB, xMatrixC)
        # calculating the matrix with x axis rotation 

        yMatrixA = Vector(cos(self.angleInRadians.y), 0, sin(self.angleInRadians.y))
        yMatrixB = Vector(0,1,0)
        yMatrixC = Vector(-sin(self.angleInRadians.y) , 0 , cos(self.angleInRadians.y))
        yMatrix = targetObj.mulMatrix(xMatrix, yMatrixA, yMatrixB, yMatrixC)
        # calculating the matrix with y axis rotation 

        zMatrixA = Vector(cos(self.angleInRadians.z), -sin(self.angleInRadians.z), 0)
        zMatrixB = Vector(sin(self.angleInRadians.z),cos(self.angleInRadians.z),0)
        zMatrixC = Vector(0,0,1)
        zMatrix = targetObj.mulMatrix(yMatrix, zMatrixA, zMatrixB, zMatrixC)
        # calculating the matrix with y axis rotation 
       
        w = zMatrix.distance(targetObj.position)
        # distance between object and camera

        return (targetObj.multiViewProjection[0]*(self.fov/w), targetObj.multiViewProjection[1]*(self.fov/w))

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
