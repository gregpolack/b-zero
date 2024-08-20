import pygame
from objects import *

HEIGHT = 1000
WIDTH = 750
FPS = 45

    
def check_state(player, screen, current_level):
    font = pygame.font.SysFont(None, 88)
    game_over_text = font.render("Game over", True, "white")
    game_won_text = font.render("You won! Thanks for playing :)", True, "white")

    levels = [
        Level(),
        LevelTwo(),
        LevelThree(),
        LevelFour(),
        LevelFive(),
        LevelSix(),
        LevelSeven()
    ]
    
    if player.rect.x < 0 or player.rect.y > 750 or player.rect.y < 0:
        text_rect = game_over_text.get_rect()
        text_rect.center = (HEIGHT // 2, WIDTH // 2)
        screen.fill("black")
        screen.blit(game_over_text, text_rect)

    for i in range(len(levels)):
        if player.rect.x >= 1000 and type(current_level) == type(levels[i]):
            if type(current_level) == type(LevelSeven()) and player.rect.x > 1000:
                text_rect = game_won_text.get_rect()
                text_rect.center = (HEIGHT // 2, WIDTH // 2)
                screen.fill("black")
                screen.blit(game_won_text, text_rect)
            else:
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
        player, current_level = check_state(player, screen, current_level)
        
        pygame.display.flip()
    
    pygame.quit()

if __name__ == "__main__":
    main()