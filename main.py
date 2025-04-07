# this allows us to use code from
# the open-source pygame library
# throughout this file
import sys
import pygame
import constants
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

#source venv/bin/activate
#python3 main.py

def main():
    pygame.init()

    gameclock = pygame.time.Clock()
    dt = 0
    target_fps = 60

    print("Starting Asteroids!")
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()


    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    player1 = Player(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2)
    field = AsteroidField()

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        #check inputs

        #update world
        updatable.update(dt)

        for rock in asteroids:
            if rock.collide(player1):
                print("Game over!")
                sys.exit()
        
        for rock in asteroids:
            for pebble in shots:
                if rock.collide(pebble):
                    rock.kill()
                    pebble.kill()


        #draw screen
        screen.fill("black")
        for thing in drawable:
            thing.draw(screen)

        #last
        pygame.display.flip()
        dt = gameclock.tick(target_fps) / 1000

if __name__ == "__main__":
    main()
