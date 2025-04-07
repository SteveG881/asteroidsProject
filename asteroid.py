import pygame
import constants
import random
from circleshape import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.wall_width = 2
        self.color = "white"

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.position, self.radius, self.wall_width)

    def update(self, delta_time):
        self.position += self.velocity * delta_time

    def split(self):
        self.kill()
        if self.radius <= constants.ASTEROID_MIN_RADIUS:
            return
        else:
            angle = random.uniform(20, 50)
            direction1 = self.velocity.rotate(angle)
            direction2 = self.velocity.rotate(-angle)
            new_radius = self.radius - constants.ASTEROID_MIN_RADIUS
            sub1 = Asteroid(self.position[0], self.position[1], new_radius)
            sub1.velocity = direction1 * 1.2
            sub2 = Asteroid(self.position[0], self.position[1], new_radius)
            sub2.velocity = direction2 * 1.2