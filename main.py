# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import constants
import player

def main():
    pygame.init()

    gameclock = pygame.time.Clock()
    dt = 0
    target_fps = 60

    print("Starting Asteroids!")
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    player1 = player.Player(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2)

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        #check inputs

        #update world

        #draw screen
        screen.fill("black")
        player1.draw(screen)

        #last
        pygame.display.flip()
        dt = gameclock.tick(target_fps) / 1000

if __name__ == "__main__":
    main()
