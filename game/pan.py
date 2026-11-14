import pygame

class pan:
    def __init__(self):
        self.image = pygame.image.load("assets/game/pan.png").convert_alpha()
        self.positions = [(500, 520), (400, 420), (300, 320), (500, 250), (650, 250)]
        self.pans = []

        for x, y in self.positions:
            pan_rect = self.image.get_rect(topleft=(x, y))
            self.pans.append(pan_rect)

        self.bounce_strength = -10

    def update(self, player):
        for pan_rect in self.pans:
            if player.rect.colliderect(pan_rect):
                if player.y_velocity > 0:
                    player.y = pan_rect.top - player.image.get_height()
                    player.y_velocity = self.bounce_strength
                    player.on_floor = False

    def draw(self, screen):
        for pan_rect in self.pans:
            screen.blit(self.image, pan_rect)
