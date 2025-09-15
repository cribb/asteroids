import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):

    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.x = x
        self.y = y
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass
    
    def collision_check(self, potential_collider):

        distance_trigger = self.radius + potential_collider.radius

        gap_distance = pygame.math.Vector2.distance_to(self.position, potential_collider.position)

        if gap_distance <= distance_trigger:            
            # print("Collision detected!")
            return True
        else:
            return False