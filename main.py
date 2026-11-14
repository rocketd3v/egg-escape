
import pygame
pygame.init()

from settings import *
from scenes.menu import *
from scenes.credits import *
from game.player import player
from game.balloon import balloon
from game.pan import pan

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("egg escape")

menu_screen = menu()
credits_screen = credits()
player_character = player()
balloons = balloon()
pans = pan()

clock = pygame.time.Clock()

run = True
current_scene = "menu"
menu_option = None

while run:
    dt = clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                current_scene = "menu"
                menu_option = None

            if event.key == pygame.K_w and current_scene == "game":
                player_character.jump()

        if current_scene == "menu":
            menu_option = menu_screen.menu_selection(event)

    if current_scene == "menu":
        if menu_option == 0:
            current_scene = "game"
            menu_option = None
        elif menu_option == 1:
            pass
        elif menu_option == 2:
            current_scene = "credits"
            menu_option = None
        elif menu_option == 3:
            run = False
        screen.fill(white)
        menu_screen.draw_menu(screen)

    elif current_scene == "credits":

        screen.fill(white)
        credits_screen.draw_credits(screen)

    elif current_scene == "game":
        screen.blit(kitchen_background, (0, 0))

        player_character.movement()
        player_character.apply_gravity(dt)

        balloons.update(player_character)
        balloons.draw(screen)

        pans.update(player_character)
        pans.draw(screen)

        player_character.animation(dt)
        player_character.draw(screen)

    pygame.display.flip()

pygame.quit()
