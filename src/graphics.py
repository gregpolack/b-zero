import pygame

class Window:
    def __init__(self, width, height):
        # pygame.init()/quit() might go to the main function depending on future behavior/interactions.
        pygame.init()
        self._screen = pygame.display.set_mode((width, height))
        

        self._clock = pygame.time.Clock()
        self._is_running = True
    
    def run(self):
        while self._is_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self._is_running = False
            
            self._screen.fill("black")

            pygame.display.flip() # Update display.
            
            self._clock.tick(60) # Limit to 60 FPS.
        
        self.close()
    
    def close(self):
        pygame.quit