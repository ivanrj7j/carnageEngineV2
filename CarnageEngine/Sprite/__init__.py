from pygame import image


class Sprite:
    def __init__(self, filePath:str, name="") -> None:
        """
        Makes a Sprite out of an image

        :param str filePath: The file path of the image to load as the sprite. Use / to split between folders
        """
        if name == "" or name==None:
            self.name = filePath.split("/")[-1].split(".")[0]
        else:
            self.name = name
        self.sprite = image.load(filePath)

    def render(self, surface):
        """
        Renders the sprite to the scene
        
        :param pygame.display surface: The surface on which the object should be rendered in
        """
        pass