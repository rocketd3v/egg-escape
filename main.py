import pygame
from settings import *
pygame.init()


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("egg escape")

title_text = pygame.font.Font("egg bounce", )

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                run = False

    screen.fill(white)
    pygame.display.flip()
