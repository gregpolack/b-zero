import pygame
from graphics import Window

def main():

    pygame.init()

    win = Window(1024,768)

    while win._is_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                win._is_running = False
        
        win._screen.fill("black")

        win._clock.tick(60)
    
    pygame.quit()

if __name__ == "__main__":
    main()