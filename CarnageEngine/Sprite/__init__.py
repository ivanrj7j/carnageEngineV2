from cmath import sqrt
import this
import pygame
from CarnageEngine.Transform import Transform 
from CarnageEngine import Entity
from CarnageEngine.Camera import Camera
from CarnageEngine.Vector import Vector



class Sprite:
    def __init__(self, filePath:str, dimensions:Vector, name="") -> None:
        """
        Makes a Sprite out of an image

        :param str filePath: The file path of the image to load as the sprite. Use / to split between folders
        """
        if name == "" or name==None:
            self.name = filePath.split("/")[-1].split(".")[0]
        else:
            self.name = name

        self.filePath = filePath
        self.dimensions = dimensions

    def render(self, surface, this:Entity, cam:Camera):
        """
        Renders the sprite to the scene
        
        :param pygame.display surface: The surface on which the object should be rendered in
        :param Entity this: The Entity to which the sprite is linked to
        """
        
        image = pygame.image.load(self.filePath)
        image = pygame.transform.scale(image, (self.dimensions.x*this.scale.x, self.dimensions.y*this.scale.y))
        surface.screen.blit(image,this.transform.vector)