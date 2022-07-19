from math import cos, radians, sin
from xml.dom.minidom import Entity
from pygame import Rect
import pygame
from CarnageEngine.Transform import Transform
from CarnageEngine.Vector import Vector


class Camera:
    def __init__(self, position=Vector(0,0), fov=45, angle=Vector(0,0)) -> None:
        """
        Acts as the eye of the Scene, all the calculations are done relative to this
        """
        self.position = position
        self.fov = fov
        self.angle = angle

    def Update(self, children, window):
        """
        Runs every time the frame is refreshed
        
        :param list children: The list of all the children:Entity in the scene
        :param Window window: The window on which the current scene is running
        :param Scene this: The Scene on which the camera is running
        """
        if len(children) > 0:
            for child in children:
                child.Update(window, self)
                
                if ("Sprite" in dir(child) or "AnimatedSprite" in dir(child)):
                    child.Sprite.render(window, child, self)
