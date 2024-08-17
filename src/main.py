import pygame
from graphics import *

def main():

    # Initial game setup.
    pygame.init()
    HEIGHT = 1000
    WIDTH = 750
    FPS = 45
    screen = pygame.display.set_mode((HEIGHT, WIDTH), pygame.SCALED | pygame.RESIZABLE)
    screen_color = "black"
    clock = pygame.time.Clock()
    is_running = True
    pygame.display.set_caption("B-Zero")

    # Initialize player and levels.
    player = Player(100, 500, 7, 7)
    level_one = Level()
    level_two = LevelTwo()
    level_three = LevelThree()
    level_four = LevelFour()
    level_five = LevelFive()
    current_level = level_one
    current_level.load_sprites()
    
    # Game loop.
    while is_running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
        screen.fill(screen_color)
        player.draw(screen)
        player.update(current_level)
        current_level.draw(screen)

        # Level switching logic.
        if player.rect.x >= 1000 and current_level == level_one:
            current_level = level_two
            player = Player(100, 250, 7, 7)
            current_level.load_sprites()
        if player.rect.x >= 1000 and current_level == level_two:
            current_level = level_three
            player = Player(100, 50, 7, 7)
            current_level.load_sprites()
        if player.rect.x >= 1000 and current_level == level_three:
            current_level = level_four
            player = Player(100, 350, 7, 7)
            current_level.load_sprites()
        if player.rect.x >= 1000 and current_level == level_four:
            current_level = level_five
            player = Player(100, 50, 7, 7)
            current_level.load_sprites()

        pygame.display.flip()
    
    pygame.quit()

if __name__ == "__main__":
    main()