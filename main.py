import pygame
pygame.init()
from settings import *
from scenes.menu import *

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("egg escape")

menu = menu()
run = True
current_scene = "menu"

while run:
    for event in pygame.event.get():
        menu_option = menu.menu_selection(event)
        if event.type == pygame.QUIT:
            run = False

    if menu_option == 0: # play
        pass
    elif menu_option == 1: # help
        pass
    elif menu_option == 2: # credits
        pass
    elif menu_option == 3: # end game
        run = False

    if current_scene == "menu":
        screen.fill(white)
    elif current_scene == "game":
        screen.fill(yellow)

    menu.draw_menu(screen)
    pygame.display.flip()
