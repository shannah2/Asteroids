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
        self.radius = radius

    def draw(self, screen):
        # must override
        pass

    def update(self, dt):
        # must override
        pass

    def collides_with(self, other):
        #Find the distance between two objects.
        distance = self.position.distance_to(other.position)
        #Add the radius of the two objects together.
        combined_radius = self.radius + other.radius
        #If the distance between the two objects is less that their combined radius
        #they must be colliding, so return true.
        if distance < combined_radius:
            return True
        else:
            return False