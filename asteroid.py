import pygame
import random
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        #If the asteroid was the minimum size or less, return, nothing left to do.
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        #If it wasn't the minimum size then we need to create new asteroids.
        log_event("asteroid_split")
        #Random angle for the new asteroids to fly out from.
        angle = random.uniform(20, 50)
        new_vector1 = self.velocity.rotate(angle)
        new_vector2 = self.velocity.rotate(-angle)

        #Compute new asteroid's radius
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        #Create the asteroids
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)

        #Set new velocity to be faster
        asteroid1.velocity = new_vector1 * 1.2
        asteroid2.velocity = new_vector2 * 1.2