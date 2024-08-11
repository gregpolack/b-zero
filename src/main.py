import pygame
from graphics import PlayerBox
from levels import LevelOne

def main():

    # Initial game setup.
    pygame.init()
    HEIGHT = 1920
    WIDTH = 1080

    screen = pygame.display.set_mode((HEIGHT, WIDTH))
    screen_color = "black"
    clock = pygame.time.Clock()
    is_running = True
    pygame.display.set_caption("B-Zero")

    # Tuples for RGB values.
    white = (255, 255, 255)
    brown = (150, 75, 0)
    
    # Initialize game objects.
    player = PlayerBox(50, 50, 20, 20, white)
    level_one = LevelOne()

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
        player.check_collision() # Not working anymore as it functions only with single rect objects.
        level_one.draw(screen)
        

        pygame.display.flip()
    
    pygame.quit()

if __name__ == "__main__":
    main()