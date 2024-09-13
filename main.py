import pygame
from constants import *


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
        screen.fill((0, 0, 0))
        pygame.display.flip()

        # limit to 60fps
        dt = clock.tick(60) / 1000

    pygame.quit()
        

if __name__ == "__main__":
    main()

