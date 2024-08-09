import pygame
from graphics import Box

def main():

    # Initial game setup.
    pygame.init()
    screen = pygame.display.set_mode((1024,768))
    screen_color = "black"
    clock = pygame.time.Clock()
    is_running = True
    pygame.display.set_caption("B-Zero")
    
    # Initialize player object.
    player = Box(30, 30, 60, 60, (255,255,255))

    # Game loop.
    while is_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
        
        screen.fill(screen_color)
        player.draw(screen)

        pygame.display.flip()

        clock.tick(60)
    
    pygame.quit()

if __name__ == "__main__":
    main()