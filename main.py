import pygame
pygame.init()
from settings import *
from scenes.menu import *

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("egg escape")

menu = menu()
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                run = False



    screen.fill(white)
    screen.blit(menu.title_surface, menu.title_rect)
    pygame.display.flip()
