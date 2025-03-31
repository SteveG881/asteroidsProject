import circleshape
import constants
import pygame

class Player(circleshape.CircleShape):
    def __init__(self, x, y):
        self.x_location = x
        self.y_location = y
        super().__init__(self.x_location, self.y_location, constants.PLAYER_RADIUS)
        
        self.rotation = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        self.color = "white"
        self.wall_width = 2

        pygame.draw.polygon(screen, self.color, self.triangle(), self.wall_width)

