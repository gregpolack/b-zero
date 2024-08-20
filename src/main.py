import pygame
from graphics import *

def check_level(player, current_level):
    levels = [
        Level(),
        LevelTwo(),
        LevelThree(),
        LevelFour(),
        LevelFive(),
        LevelSix(),
        LevelSeven()
    ]
    
    for i in range(len(levels)):
        if player.rect.x >= 1000 and type(current_level) == type(levels[i]):
            current_level = levels[i+1]
            current_level.load_sprites()
            if type(current_level) == type(LevelTwo()):
                player = Player(100, 250, 7, 7)
            elif type(current_level) == type(LevelFour()):
                player = Player(100, 250, 7, 7)
            elif type(current_level) == type(LevelSix()):
                player = Player(800, 50, 7, 7)
            elif type(current_level) == type(LevelSeven()):
                player = Player(100, 500, 7, 7)
            else:
                player = Player(100, 50, 7, 7)
                   
    return player, current_level

def main():

    # Initial game setup.
    pygame.init()
    HEIGHT = 1000
    WIDTH = 750
    FPS = 45
    font = pygame.font.SysFont(None, 88)
    text = font.render("Game over", True, "white")
    text_rect = text.get_rect()
    text_rect.center = (HEIGHT // 2, WIDTH // 2)
    screen = pygame.display.set_mode((HEIGHT, WIDTH), pygame.SCALED | pygame.RESIZABLE)
    screen_color = "black"
    clock = pygame.time.Clock()
    is_running = True
    pygame.display.set_caption("B-Zero")

    # Initialize player and levels.
    player = Player(100, 500, 7, 7)
    current_level = Level()
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

        player, current_level = check_level(player, current_level)

        # Check for game over state.
        if player.rect.x < 0 or player.rect.y > 750 or player.rect.y < 0:
            screen.fill(screen_color)
            screen.blit(text, text_rect)
    
        pygame.display.flip()
    
    pygame.quit()

if __name__ == "__main__":
    main()