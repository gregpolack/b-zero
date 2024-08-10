import pygame

class Box:
    def __init__(
            self, 
            pos_x: float, 
            pos_y: float, 
            width: float, 
            height: float,
            color: tuple
    ):
        self._rect = pygame.rect.Rect((pos_x, pos_y, width, height))
        self._color = color 
    
    def draw(self, surface: pygame.Surface):
        pygame.draw.rect(surface, self._color, self._rect)

class PlayerBox(Box):
    def __init__(
            self, 
            pos_x: float, 
            pos_y: float, 
            width: float, 
            height: float, 
            color: tuple
    ):
        super().__init__(
            pos_x,
            pos_y,
            width,
            height,
            color
        )
        self.gravity = 0

    def handle_keys(self):
        key = pygame.key.get_pressed()
        dist = 5
        if key[pygame.K_LEFT]:
            self._rect.move_ip(-dist, 0)
        if key[pygame.K_RIGHT]:
            self._rect.move_ip(dist, 0)
    
    def apply_gravity(self):
        self.gravity += 1
        self._rect.move_ip(0, self.gravity)
    
    def check_collision(self, rect: pygame.Rect):
        collide = pygame.Rect.colliderect(self._rect, rect._rect)

        if collide:
            self.gravity = -20

                        
class FloorBox(Box):
    def __init__(
            self,
            pos_x: float,
            pos_y: float,
            width: float,
            height: float,
            color: tuple
    ):
        super().__init__(
            pos_x,
            pos_y,
            width,
            height,
            color
        )

