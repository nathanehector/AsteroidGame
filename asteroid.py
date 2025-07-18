import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.radius = radius

    def draw(self, surface):
        pygame.draw.circle(surface, (255, 255, 255), self.position, self.radius, width = 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        import math
        from asteroid import Asteroid


        new_radius = self.radius - ASTEROID_MIN_RADIUS

        angle = random.uniform(20,50)

        dir1 = self.velocity.rotate(angle) * 1.2
        dir2 = self.velocity.rotate(-angle) * 1.2


        Asteroid(self.position.x, self.position.y, new_radius).velocity = dir1
        Asteroid(self.position.x, self.position.y, new_radius).velocity = dir2
