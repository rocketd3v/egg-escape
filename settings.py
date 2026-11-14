import pygame

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 750

white = 255, 255, 255
yellow = 255, 215, 0
black = 144, 144, 144

egg_font = "/Users/rocket/Desktop/egg_escape/assets/fonts/egg_font.ttf"

kitchen_background = pygame.image.load("assets/game/kitchen.png")
kitchen_background = pygame.transform.scale(kitchen_background, (SCREEN_WIDTH, SCREEN_HEIGHT))

