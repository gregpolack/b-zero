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
    level_six = LevelSix()
    level_seven = LevelSeven()
    font = pygame.font.SysFont(None, 88)
    text = font.render("Game over", True, "white")
    text_rect = text.get_rect()
    text_rect.center = (HEIGHT // 2, WIDTH // 2)
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
        if player.rect.x >= 1000 and current_level == level_five:
            current_level = level_six
            player = Player(800, 50, 7, 7)
            current_level.load_sprites()
        if player.rect.x >= 1000 and current_level == level_six:
            current_level = level_seven
            player = Player(100, 500, 7, 7)
            current_level.load_sprites()
        if player.rect.x < 0 or player.rect.y > 750 or player.rect.y < 0:
            screen.fill(screen_color)
            screen.blit(text, text_rect)
            
        pygame.display.flip()
    
    pygame.quit()

if __name__ == "__main__":
    main()