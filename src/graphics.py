import pygame

class Box:
    def __init__(self, pos_x: float, pos_y: float, width: float, height: float, color: tuple):
        self._color = color
        self.pos_x = pos_x
        self.pos_y = pos_y
        self._width = width
        self._height = height
    
    def draw(self, win: pygame.Surface):
        pygame.draw.rect(win, 
                         self._color, 
                         pygame.Rect(self.pos_x, 
                                     self.pos_y, 
                                     self._width, 
                                     self._height))