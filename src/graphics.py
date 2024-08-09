import pygame

class Window:
    def __init__(self, width, height):
        self._screen = pygame.display.set_mode((width, height))
        self._clock = pygame.time.Clock()
        self._is_running = True
        pygame.display.set_caption("B-Zero")    

class Box:
    def __init__(self, pos_x, pos_y, width, height):
        self._color = (255, 255, 255)
        self.pos_x = pos_x
        self.pos_y = pos_y
        self._width = width
        self._height = height
    
    def draw(self, win):
        pygame.draw.rect(win, 
                         self._color, 
                         pygame.Rect(self.pos_x, 
                                     self.pos_y, 
                                     self._width, 
                                     self._height))