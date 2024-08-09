import pygame
from graphics import PlayerBox, FloorBox

def main():

    # Initial game setup.
    pygame.init()
    screen = pygame.display.set_mode((1024,768))
    screen_color = "black"
    clock = pygame.time.Clock()
    is_running = True
    pygame.display.set_caption("B-Zero")

    # Tuples for RGB values.
    white = (255, 255, 255)
    brown = (150, 75, 0)
    
    # Initialize game objects.
    player = PlayerBox(50, 50, 20, 20, white)
    floor = FloorBox(0, 1000, 60, 60, brown)

    # Game loop.
    while is_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_F11:
                pygame.display.toggle_fullscreen()
        
        screen.fill(screen_color)
        player.draw(screen)
        player.handle_keys()
        floor.draw(screen)

        pygame.display.flip()

        clock.tick(60)
    
    pygame.quit()

if __name__ == "__main__":
    main()