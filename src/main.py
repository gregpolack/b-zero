import pygame
from graphics import Player, LevelOne

def main():

    # Initial game setup.
    pygame.init()
    HEIGHT = 1000
    WIDTH = 750
    FPS = 45

    screen = pygame.display.set_mode((HEIGHT, WIDTH))
    screen_color = "black"
    clock = pygame.time.Clock()
    is_running = True
    pygame.display.set_caption("B-Zero")

    # Initialize game objects.
    player = Player(100, 500, 10, 10)
    level = LevelOne()

    # Game loop.
    
    while is_running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
        
        screen.fill(screen_color)
        player.draw(screen)
        player.update(level)
        level.draw(screen)
    
        pygame.display.flip()
    
    pygame.quit()

if __name__ == "__main__":
    main()