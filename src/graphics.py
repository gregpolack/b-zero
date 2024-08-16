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
        self.speed = 5
        self.direction = pygame.Vector2()
        self.gravity_applied = True
        self.left_bounce_timer = Timer(150)
        self.right_bounce_timer = Timer(150)
        
    def handle_keys(self):
        self.key = pygame.key.get_pressed()
        
        self.direction.x = int(self.key[pygame.K_RIGHT]) - int(self.key[pygame.K_LEFT])
        self.rect.center += self.direction * self.speed

    def apply_gravity(self):
        if self.gravity_applied:
            self.force = 0
            self.gravity += 0.8
            self.rect.move_ip(0, self.gravity)
        
    def apply_force(self):
        self.rect.move_ip(self.force, 0)
        
    def check_collisions(self, level):

        collision_threshold = 17
        
        collide_rock = pygame.sprite.spritecollide(self, level.rocks, dokill=True)
        collide_floor = pygame.sprite.spritecollide(self, level.floor, dokill=False)

        if collide_floor:
            collided_sprite = collide_floor[0]
            if abs(self.rect.bottom - collided_sprite.rect.top) < collision_threshold:
                self.gravity = -13
            elif abs(self.rect.right - collided_sprite.rect.left) < collision_threshold:
                    self.left_bounce_timer.activate()
            elif abs(self.rect.left - collided_sprite.rect.right) < collision_threshold:
                    self.right_bounce_timer.activate()

        self.left_bounce_timer.update()
        self.right_bounce_timer.update()

        if self.left_bounce_timer.is_active:
            self.disable_input_and_lift()
            self.force = -13
        elif self.right_bounce_timer.is_active:
            self.disable_input_and_lift()
            self.force = 13
        else:
            self.gravity_applied = True
    
        if collide_rock:
            self.gravity = -13

    def disable_input_and_lift(self):
        pygame.event.set_blocked([self.key[pygame.K_LEFT]])
        pygame.event.set_blocked([self.key[pygame.K_RIGHT]])
        self.gravity_applied = False
        self.rect.move_ip(0, -2)
        
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

class Boost(Box):
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
        self.image = pygame.image.load("./assets/Arrow_box.jpg").convert()

class Level:
    layout = [
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,1,1,1,2,2,1,1,1],
            [1,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0,0,0],
            [1,0,0,0,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
        ]
    def __init__(self):
        self.num_rows = 15
        self.num_cols = 20
        self.floor = pygame.sprite.Group()
        self.rocks = pygame.sprite.Group()
        self.boosts = pygame.sprite.Group()
    
    def load_sprites(self):
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                if self.layout[i][j] == 1:
                    floor_tile = Floor(j * 50, i * 50, 50, 50)
                    self.floor.add(floor_tile)
                if self.layout[i][j] == 2:
                    rock_tile = Rock(j * 50, i * 50, 50, 50)
                    self.rocks.add(rock_tile)
                if self.layout[i][j] == 3:
                    boost = Boost(j * 50, i * 50, 50, 50)
                    self.boosts.add(boost)

    def draw(self, screen):
        self.groups = [
            self.floor,
            self.rocks,
            self.boosts
        ]

        for group in self.groups:
            group.draw(screen)
    
class LevelTwo(Level):
    layout = [
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [1,1,1,1,0,0,0,0,0,1,1,1,1,0,1,1,1,1,1,1],
            [1,1,1,1,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,1],
            [1,1,1,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,1,1,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,1,1,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,1]
        ]
        
    def __init__(self):
        super().__init__()

class LevelThree(Level):
    layout = [
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,1,1,1,1,1,0,2,2,1,1,1,1,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,1,1,1,1,2,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,1,1,1,1,3,0,0,0,0],
            [1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1]
        ]
        
    def __init__(self):
        super().__init__()