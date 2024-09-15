import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import AsteroidField
from shot import Shot


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    field = AsteroidField()

    Shot.containers = (shots, updatable, drawable)

    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
        screen.fill((0, 0, 0))
        for item in drawable:
            item.draw(screen)

        for item in updatable:
            item.update(dt)
            

        for asteroid in asteroids:
            #and object is type(Player)
            if player.collides(asteroid):
                print("Game Over")
                running = False
            for bullet in shots:
                if asteroid.collides(bullet):
                    asteroid.split()
                    bullet.kill() 


        pygame.display.flip()
        
        # limit to 60fps
        dt = clock.tick(60) / 1000
    

    pygame.quit()
        

if __name__ == "__main__":
    main()

