import pygame
from timer import Timer

class Box(pygame.sprite.Sprite):
    def __init__(
            self, 
            pos_x: float, 
            pos_y: float, 
            width: float, 
            height: float,
            color = None 
    ):
        super().__init__()
        self.rect = pygame.rect.Rect((pos_x, pos_y, width, height))
        self._color = color 
    
    def draw(self, surface: pygame.Surface):
        pygame.draw.rect(surface, self._color, self.rect)

class Player(Box):
    def __init__(
            self, 
            pos_x: float, 
            pos_y: float, 
            width: float, 
            height: float
    ):
        super().__init__(
            pos_x,
            pos_y,
            width,
            height
        )
        self._color = (255, 255, 255) # White.
        self.gravity = 0
        self.force = 0
        self.gravity_applied = True
        self.left_bounce_timer = Timer(150)
        self.right_bounce_timer = Timer(150)
        
    def handle_keys(self):
        self.key = pygame.key.get_pressed()
        dist = 5
        if self.key[pygame.K_LEFT]:
            self.rect.move_ip(-dist, 0)
        if self.key[pygame.K_RIGHT]:
            self.rect.move_ip(dist, 0)
    
    def apply_gravity(self):
        if self.gravity_applied:
            self.force = 0
            self.gravity += 0.75
            self.rect.move_ip(0, self.gravity)
        
    def apply_force(self):
        self.rect.move_ip(self.force, 0)
        
    def check_collisions(self, level):
        collide_rock = pygame.sprite.spritecollide(self, level.rock_tiles, dokill=True)
        collide_floor = pygame.sprite.spritecollide(self, level.floor_tiles, dokill=False)
        collide_left_wall = pygame.sprite.spritecollide(self, level.left_wall_tiles, dokill=False)
        collide_right_wall = pygame.sprite.spritecollide(self, level.right_wall_tiles, dokill=False)
        
        if collide_floor or collide_rock:
            self.gravity = -13
        if collide_left_wall:
            self.left_bounce_timer.activate()
        if collide_right_wall:
            self.right_bounce_timer.activate()

        self.left_bounce_timer.update()
        self.right_bounce_timer.update()

        if self.left_bounce_timer.is_active:
            self.disable_input_and_lift()
            self.force = 13
        elif self.right_bounce_timer.is_active:
            self.disable_input_and_lift()
            self.force = -13
        else:
            self.gravity_applied = True
    
    def disable_input_and_lift(self):
        pygame.event.set_blocked([self.key[pygame.K_LEFT]])
        pygame.event.set_blocked([self.key[pygame.K_RIGHT]])
        self.gravity_applied = False
        self.rect.move_ip(0, -5)
        
    def update(self, level):
        self.handle_keys()
        self.apply_gravity()
        self.apply_force()
        self.check_collisions(level)
                        
class Floor(Box):
    def __init__(
            self,
            pos_x: float,
            pos_y: float,
            width: float,
            height: float,
            color = None 
    ):
        super().__init__(
            pos_x,
            pos_y,
            width,
            height,
            color
        )
        self.image = pygame.image.load("./assets/Box.jpg").convert()

class Rock(Box):
    def __init__(
            self,
            pos_x: float,
            pos_y: float,
            width: float,
            height: float,
            color = None 
    ):
        super().__init__(
            pos_x,
            pos_y,
            width,
            height,
            color
        )
        self.image = pygame.image.load("./assets/Rock.jpg").convert()

class LevelOne:
    def __init__(self):
        self.game_level = [
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4],
            [3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4],
            [3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4],
            [3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4],
            [3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4],
            [3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4],
            [3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4],
            [3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4],
            [3,0,0,0,0,0,0,0,0,0,0,0,1,1,1,2,2,1,1,1],
            [3,0,0,0,0,0,0,0,0,1,1,1,3,0,0,0,0,0,0,4],
            [3,0,0,0,0,0,0,1,1,1,1,1,3,0,0,0,0,0,0,0],
            [3,0,0,0,1,1,1,1,1,1,1,1,3,0,0,0,0,0,0,0],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
        ]
        self.num_rows = 15
        self.num_cols = 20
        self.floor_tiles = pygame.sprite.Group()
        self.rock_tiles = pygame.sprite.Group()
        self.left_wall_tiles = pygame.sprite.Group()
        self.right_wall_tiles = pygame.sprite.Group()
        
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                if self.game_level[i][j] == 1:
                    floor_tile = Floor(j * 50, i * 50, 50, 50)
                    self.floor_tiles.add(floor_tile)
                if self.game_level[i][j] == 2:
                    rock_tile = Rock(j * 50, i * 50, 50, 50)
                    self.rock_tiles.add(rock_tile)
                if self.game_level[i][j] == 3:
                    left_wall_tile = Floor(j * 50, i * 50, 50, 50)
                    self.left_wall_tiles.add(left_wall_tile)
                if self.game_level[i][j] == 4:
                    right_wall_tile = Floor(j * 50, i * 50, 50, 50)
                    self.right_wall_tiles.add(right_wall_tile)
    
    def draw(self, screen):
        self.groups = [
            self.floor_tiles,
            self.rock_tiles,
            self.left_wall_tiles,
            self.right_wall_tiles
        ]

        for group in self.groups:
            group.draw(screen)