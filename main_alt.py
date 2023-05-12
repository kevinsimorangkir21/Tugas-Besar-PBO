# Modules
import pygame
import random
from modules import Menu


# PYGAME INIT
pygame.init()

# Display Setting
SIZE = (1280, 720)
icon = pygame.image.load("assets/images/icon.png")
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Lost")
pygame.display.set_icon(icon)

# Menu loop


def menu_loop():
    current_menu = "main_menu"

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                # Menu button clicks
                current_menu = Menu.change_menu(
                    menu_dict, current_menu, screen)

                # Exit menu
                if current_menu not in menu_dict:
                    return current_menu

        pygame.display.update()

# Main function


def main():
    current_loop = "menu"

    while True:
        if current_loop == "menu":
            current_loop = menu_loop()

        if current_loop == "<exit>":
            break

    pygame.quit()


if __name__ == "__main__":
    main()
