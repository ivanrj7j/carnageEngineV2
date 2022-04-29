import pygame

class Window:
    def __init__(self, dimensions:tuple,scenes:dict, currentScene, title="Carnage Window", backgroundColor = (181,51,83)) -> None:
        self.dimensions = dimensions
        self.backgroundColor = backgroundColor
        self.title = title
        self.scenes = scenes
        self.currentScene = scenes[currentScene]
        self.screen = pygame.display.set_mode(self.dimensions)
        pygame.display.set_caption(self.title)
        self.clock = pygame.time.Clock()
        self.running = True

    def Update(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.currentScene.Exit()
                    self.running = False

            self.screen.fill(self.backgroundColor)
            #clear the screen

            self.currentScene.Update()
            # updating the current scene 

            pygame.display.flip()
            # flip() updates the screen to make our changes visible
     
            self.clock.tick(60)
            # how many updates per second
        pygame.quit()