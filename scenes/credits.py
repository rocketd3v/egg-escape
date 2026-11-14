
import pygame
pygame.init()

from settings import *

class credits():
    def __init__(self):
        self.credits = ["Ahmad - programming", "Chris - artwork", "Ayo - game idea", "Ahmed - game testing", "Mohamed - more intensive tester"]
        
        self.title_font = pygame.font.Font(egg_font, 76)
        self.menu_font = pygame.font.Font(egg_font, 46)

        self.title_surface = self.title_font.render("CREDITS", True, yellow)
        self.title_rect = self.title_surface.get_rect()
        self.title_rect.centerx = 500
        self.title_rect.centery = 50

    def draw_credits(self, screen):
        screen.blit(self.title_surface, self.title_rect)

        for i in range(len(self.credits)):
            text_surface = self.menu_font.render(self.credits[i], True, black)

            text_rect = text_surface.get_rect()
            text_rect.centerx = SCREEN_WIDTH // 2
            text_rect.centery = 250 + (i * 80)

            screen.blit(text_surface, text_rect)
