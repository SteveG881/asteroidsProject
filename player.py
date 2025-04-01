from circleshape import *
import constants
import pygame

class Player(CircleShape):
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

    def rotate(self, delta_time):
        self.rotation += constants.PLAYER_TURN_RATE * delta_time

    def update(self, delta_time):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(delta_time * -1)
        if keys[pygame.K_d]:
            self.rotate(delta_time)
        if keys[pygame.K_w]:
            self.move(delta_time)
        if keys[pygame.K_s]:
            self.move(delta_time * -1)

    def move(self, delta_time):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * constants.PLAYER_MOVE_RATE * delta_time