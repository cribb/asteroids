from constants import *
from circleshape import *
import pygame
import random

class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def update(self, dt):
        self.position += self.velocity * dt

    def draw(self, screen):
        pygame.draw.circle(screen, 
                           color="white", 
                           center=self.position, 
                           radius=self.radius,
                           width=2)
        
    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        glancing_angle = random.uniform(20, 50)
        
        vel1 = self.velocity.rotate(glancing_angle)
        vel2 = self.velocity.rotate(-glancing_angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        asteroid1.Asteroid(self.position.x, self.position.y, new_radius)
        asteroid1.velocity = vel1 * 1.2

        asteroid2.Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2.velocity = vel2 * 1.2

        
        

    
        
        