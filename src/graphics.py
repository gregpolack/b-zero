import pygame

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

class PlayerBox(Box):
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
        
    def handle_keys(self):
        key = pygame.key.get_pressed()
        dist = 5
        if key[pygame.K_LEFT]:
            self.rect.move_ip(-dist, 0)
        if key[pygame.K_RIGHT]:
            self.rect.move_ip(dist, 0)
    
    def apply_gravity(self):
        if self.gravity_applied:
            self.force = 0
            self.gravity += 0.75
            self.rect.move_ip(0, self.gravity)
        
    def apply_force(self):
        self.rect.move_ip(self.force, 0)
        
    def check_floor_collision(self, group):
        collide = pygame.sprite.spritecollide(self, group, dokill=False)

        if collide:
            self.gravity = -13
    
    def check_rock_collision(self, group):
        collide = pygame.sprite.spritecollide(self, group, dokill=True)

        if collide:
            self.gravity = -13

    def update(self):
        self.handle_keys()
        self.apply_gravity()
        self.apply_force()
                        
class FloorBox(Box):
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

class RockBox(Box):
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
            [3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3],
            [3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3],
            [3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3],
            [3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3],
            [3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3],
            [3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3],
            [3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3],
            [3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3],
            [3,0,0,0,0,0,0,0,0,0,0,0,1,1,1,2,2,1,1,1],
            [3,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,3],
            [3,0,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0,0,0],
            [3,0,0,0,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
        ]
        self.num_rows = 15
        self.num_cols = 20
        self.floor_tiles = pygame.sprite.Group()
        self.rock_tiles = pygame.sprite.Group()
        self.wall_tiles = pygame.sprite.Group()
        
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                if self.game_level[i][j] == 1:
                    floor_tile = FloorBox(j * 50, i * 50, 50, 50)
                    self.floor_tiles.add(floor_tile)
                if self.game_level[i][j] == 2:
                    rock_tile = RockBox(j * 50, i * 50, 50, 50)
                    self.rock_tiles.add(rock_tile)
                if self.game_level[i][j] == 3:
                    wall_tile = FloorBox(j * 50, i * 50, 50, 50)
                    self.wall_tiles.add(wall_tile)
