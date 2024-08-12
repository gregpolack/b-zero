import pygame
from graphics import PlayerBox, LevelOne

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

    # Game loop.
    while is_running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
        
        screen.fill(screen_color)
        player.draw(screen)
        player.apply_gravity()
        player.handle_keys()
        level.floor_tiles.draw(screen)
        level.rock_tiles.draw(screen)
        player.check_floor_collision(level.floor_tiles)
        player.check_rock_collision(level.rock_tiles)
        
        pygame.display.flip()
    
    pygame.quit()

if __name__ == "__main__":
    main()