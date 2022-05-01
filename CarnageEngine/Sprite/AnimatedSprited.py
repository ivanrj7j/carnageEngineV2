from pygame import image


class AnimatedSprite:
    def __init__(self, sprites:dict, name:str) -> None:
        """
        Makes an animated sprite with the given images

        :param dict sprites: The dictionary with the sprite's file path as the index and the duration of the
        sprite in Frame (int) as the value
        """
        self.sprites = {}
        for sprite in sprites:
            self.sprites[image.load(sprite)] = sprites[sprite]
        self.name = name

    def render(self, surface):
        """
        Renders the sprite to the scene
        
        :param pygame.display surface: The surface on which the object should be rendered in
        """
        pass