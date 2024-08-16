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
        self.boost_timer = Timer(1000)
        
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
        collide_boost = pygame.sprite.spritecollide(self, level.h_boosts, dokill=False)

        # Floor collision.
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

        # Rock collision.
        if collide_rock:
            self.gravity = -13
        
        # Boost collision.
        if collide_boost:
            collided_sprite = collide_boost[0]
            self.rect.y = collided_sprite.rect.y + 15
            self.rect.x = collided_sprite.rect.x + 50
            self.boost_timer.activate()
        
        self.boost_timer.update()
        if self.boost_timer.is_active:
            self.gravity_applied = False
            self.gravity = 0
            self.force = 16

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

class HorizontalBoost(Box):
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

class JumpBoost(Box):
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
        self.image = pygame.image.load("./assets/JumpBoost.jpg").convert()

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
        self.h_boosts = pygame.sprite.Group()
        self.j_boosts = pygame.sprite.Group()
    
    def load_sprites(self):
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                if self.layout[i][j] == 1:
                    self.floor.add(Floor(j * 50, i * 50, 50, 50))
                if self.layout[i][j] == 2:
                    self.rocks.add(Rock(j * 50, i * 50, 50, 50))
                if self.layout[i][j] == 3:
                    self.h_boosts.add(HorizontalBoost(j * 50, i * 50, 50, 50))
                if self.layout[i][j] == 4:
                    self.j_boosts.add(JumpBoost(j * 50, i * 50, 50, 50))

    def draw(self, screen):
        self.groups = [
            self.floor,
            self.rocks,
            self.h_boosts,
            self.j_boosts
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

class LevelFour(Level):
    layout = [
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [1,0,0,0,0,0,0,0,0,1,1,1,0,0,1,1,1,1,1,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,4,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,1],
            [1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1]
        ]
        
    def __init__(self):
        super().__init__()