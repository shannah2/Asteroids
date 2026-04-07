import pygame

class Score(pygame.sprite.Sprite):
    def __init__(self):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        self.score = 0
        self.font = pygame.font.SysFont(None, 50)
        self.position = pygame.Vector2(0,1)

    def draw(self, screen):
        text = f"Score: {self.score}"
        image = self.font.render(text, True, "green")
        screen.blit(image, (self.position.x, self.position.y))

    def update(self, points):
        self.score += points