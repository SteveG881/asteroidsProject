import pygame
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