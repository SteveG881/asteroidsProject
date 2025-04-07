import pygame
import constants
from circleshape import *

class Shot(CircleShape):
    def __init__(self, x, y, direction, radius):
        super().__init__(x, y, radius)
        self.wall_width = 20
        self.color = "white"
        self.rotation = direction
        self.aim = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position = pygame.Vector2(x,y)
        self.velocity = pygame.Vector2(self.aim, 0)

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.position, self.radius, self.wall_width)

    def update(self, delta_time):
        self.position += self.aim * constants.PLAYER_SHOOT_SPEED * delta_time
