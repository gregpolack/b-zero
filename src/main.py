import pygame
from graphics import PlayerBox, LevelOne
from timer import Timer

def main():

    # Initial game setup.
    pygame.init()
    HEIGHT = 1000
    WIDTH = 750

    screen = pygame.display.set_mode((HEIGHT, WIDTH))
    screen_color = "black"
    clock = pygame.time.Clock()
    is_running = True
    pygame.display.set_caption("B-Zero")

    # Initialize game objects.
    player = PlayerBox(100, 500, 10, 10)
    level = LevelOne()
    timer = Timer(150)
    key = pygame.key.get_pressed()

    # Game loop.
    
    while is_running:
        clock.tick(45)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
        
        screen.fill(screen_color)
        player.draw(screen)
        player.update()
        player.check_collisions(level)
        level.floor_tiles.draw(screen)
        level.rock_tiles.draw(screen)
        level.wall_tiles.draw(screen)

        # Wall collision logic.
        collide_wall = pygame.sprite.spritecollide(player, level.wall_tiles, dokill=False)
        if collide_wall:
            timer.activate()
        
        timer.update()
        if timer.is_active:
            pygame.event.set_blocked([key[pygame.K_LEFT]])
            pygame.event.set_blocked([key[pygame.K_RIGHT]])
            player.gravity_applied = False
            player.rect.move_ip(0, -5)
            player.force = 13
        else:
            player.gravity_applied = True

        pygame.display.flip()
    
    pygame.quit()

if __name__ == "__main__":
    main()