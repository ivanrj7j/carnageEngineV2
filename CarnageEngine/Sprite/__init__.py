from pygame import image
from pygame.rect import Rect
from pygame import transform
from PIL import Image
from CarnageEngine.Transform import Transform 
from CarnageEngine.Vector import Vector



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

    def render(self, surface, this, camAngle:Vector):
        """
        Renders the sprite to the scene
        
        :param pygame.display surface: The surface on which the object should be rendered in
        :param Entity this: The Entity to which the sprite is linked to
        """
        
        img = Image.open(self.filePath).convert("RGBA")
        self.image = Image.new('RGBA', img.size, (0,0,0,0))
        for x in range(img.width):
            for z in range(img.height):
                t = this.Transform.position - this.Transform.anchor
                initPos = Transform.rotationMatrix(Vector(t.x + x, t.y, t.z + z), this.Transform.angleInRadians)
                t2 = this.Transform.anchor + initPos
                fPos = Transform.rotationMatrix(t2, camAngle)
                pos = fPos-t
                self.image.putpixel((int(pos.x), int(pos.z)), img.getpixel((x,z)))
        self.sprite = image.frombuffer(self.image.tobytes(), self.image.size, self.image.mode)
                    
        if self.dimensions:
            self.sprite = transform.scale(self.sprite, (self.dimensions[0]*this.Transform.scale.x, self.dimensions[1]*this.Transform.scale.z))


        hitbox = Rect(this.Transform.transform.x, this.Transform.transform.z, self.sprite.get_width()*this.Transform.scale.x, self.sprite.get_height()*this.Transform.scale.z)
        surface.screen.blit(self.sprite, hitbox)
        # draw.rect(surface.screen, (0,0,0), hitbox)