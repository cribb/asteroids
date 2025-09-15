from constants import *
from circleshape import *
import pygame

class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, 
                           color="white", 
                           center=self.position, 
                           radius=self.radius,
                           width=2)
        
    # Override the update() method so that it moves in a straight line at constant speed. 
    # On each frame, it should add (self.velocity * dt) to its position (get self.velocity from
    # its parent class, CircleShape).
    def update(self, dt):
        self.position += self.velocity * dt

    
