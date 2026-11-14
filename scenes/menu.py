import pygame
pygame.init()

from settings import *

class menu():
    def __init__(self):
        self.options = ["1. Play", "2. Help" ,"3. Credits", "4. Quit"]
        self.option = 0 
        self.title_text = pygame.font.Font(egg_font, 76)
        self.title_surface = self.title_text.render("Main menu", True, yellow)
        self.title_rect = self.title_surface.get_rect()
        self.title_rect.centerx = 500
        self.title_rect.centery = 50
