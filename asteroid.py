from circleshape import CircleShape
from constants import *
import random
import pygame

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        #self.velocity = pygame.Vector2(0, 0)

    def draw (self, screen):
        pygame.draw.circle (screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        random_angle = random.uniform(20, 50)
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        new_vec1 = pygame.math.Vector2.rotate(self.velocity, random_angle)
        new_vec2 = pygame.math.Vector2.rotate(self.velocity, -random_angle)
        split_radius = self.radius - ASTEROID_MIN_RADIUS
        new_asteroid1 = Asteroid(self.position.x, self.position.y, split_radius)
        new_asteroid1.velocity = new_vec1 * 1.2
        new_asteroid2 = Asteroid(self.position.x, self.position.y, split_radius)
        new_asteroid2.velocity = new_vec2 * 1.2