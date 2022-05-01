import pickle
import pygame

class Window:
    def __init__(self, dimensions:tuple,scenes:dict, currentScene, title="Carnage Window", backgroundColor = (181,51,83), logo="CarnageEngine/resource/logo.ico") -> None:
        """
        The main Window where everything happens.

        :param tuple dimensions: The width and height of the window
        :param dict scenes: The list of all Scenes used in the game
        :param Any currentScene: The index of the current scene used
        :param str title: The name of the Window (default "Carnage Window")
        :param tuple backgroundColor: The Main color which is going to be used when refreshing the frame as background (default (181,51,83))
        :param str logo: The file path of the logo (default "CarnageEngine/resource/logo.ico")
        """
        self.dimensions = dimensions
        self.backgroundColor = backgroundColor
        self.title = title
        self.scenes = scenes
        self.currentScene = scenes[currentScene]
        self.screen = pygame.display.set_mode(self.dimensions)
        # initialising the screen 
        pygame.display.set_caption(self.title)
        # setting the caption of the window 
        self.clock = pygame.time.Clock()
        # initialising the clock 
        self.running = True
        # True when the window is running 

        pygame_icon = pygame.image.load(logo)
        pygame.display.set_icon(pygame_icon)
        # setting the icon of the window

    def Update(self):
        """
        Updates the scenes every frame
        """
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.Exit()
                    # Exiting the window when the 'x' button in the window is clicked

            self.screen.fill(self.backgroundColor)
            #clear the screen

            self.currentScene.Update(self)
            # updating the current scene 

            pygame.display.flip()
            # flip() updates the screen to make our changes visible
     
            self.clock.tick(60)
            # how many updates per second
        pygame.quit()
        # quitting out of pygame 

    def CreateSave(self, destination:str):
        """
        Saves itself in the given destination

        :param str destination: The file path to where the file should be saved
        """
        with open(destination+"/"+self.name + "_"+ self.id+".carng", "wb") as saveFile:
            pickle.dump(self.__dict__, saveFile)

    @classmethod
    def InitiateFromFile(cls, file:str):
        """
        Reads the File and creates itself with the given attributes in the files

        :param str file: The path to the file
        """
        with open(file, "rb") as saveFile:
            attributes = pickle.load(saveFile)
        for attribute in attributes:
            setattr(cls, attribute, attributes[attribute])
        return cls

    def Exit(self):
        """Exits out of the window"""
        self.currentScene.Exit()
        self.running = False