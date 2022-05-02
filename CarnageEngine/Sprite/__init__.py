from pygame import image
from pygame.rect import Rect
from pygame import draw
from pygame import transform


class Sprite:
    def __init__(self, filePath:str, dimensions, name="") -> None:
        """
        Makes a Sprite out of an image

        :param str filePath: The file path of the image to load as the sprite. Use / to split between folders
        :param tuple dimensions: The dimensions of the image, if None, the default dimensions are used
        """
        if name == "" or name==None:
            self.name = filePath.split("/")[-1].split(".")[0]
        else:
            self.name = name

        self.filePath = filePath
        self.dimensions = dimensions

    def render(self, surface, this):
        """
        Renders the sprite to the scene
        
        :param pygame.display surface: The surface on which the object should be rendered in
        :param Entity this: The Entity to which the sprite is linked to
        """
        if not self.dimensions:
            self.sprite = image.load(self.filePath)
        if self.dimensions:
            self.sprite = transform.scale(image.load(self.filePath), (self.dimensions[0]*this.Transform.scale.x, self.dimensions[1]*this.Transform.scale.z))


        hitbox = Rect(this.Transform.transform.x, this.Transform.transform.z, self.sprite.get_width()*this.Transform.scale.x, self.sprite.get_height()*this.Transform.scale.z)
        surface.screen.blit(self.sprite, hitbox)
        # draw.rect(surface.screen, (0,0,0), hitbox)