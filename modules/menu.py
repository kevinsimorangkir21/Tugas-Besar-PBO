from abc import ABC, abstractmethod
import pygame
import sys
from modules.button import Button

pygame.mixer.init(buffer=64)
TITLE = "Lost"

MENU_BG = (8, 32, 50)
GAME_BG = (1, 0, 6)


class Menu(ABC):

    click_sound = pygame.mixer.Sound("assets/sounds/click.wav")
    click_sound.set_volume(0.2)

    def __init__(self, name):
        self.name = name

        # Logo dijadikan atribut kelas parent
        self.logo_pbb = pygame.image.load("assets/images/logo_chuakz.png")
        self.logo_img = pygame.image.load("assets/images/lost_logo.png")

    @abstractmethod
    def render(self):
        pass


class Main(Menu):
    def __init__(self):
        super().__init__("main_menu")

        # info_img = pygame.image.load("assets/button/info_btn.png")
        play_img = pygame.image.load("assets/button/play_button.png")
        about_img = pygame.image.load("assets/button/about_button.png")
        exit_img = pygame.image.load("assets/button/exit_button.png")

        # self.info_btn = button(image=info_img, pos=(1220, 15))
        self.play_btn = Button(image=play_img, pos=(505, 400))
        self.about_btn = Button(image=about_img, pos=(505, 465))
        self.exit_btn = Button(image=exit_img, pos=(505, 530))

    def render(self, screen):
        screen.fill(MENU_BG)

        self.logo_chuakz.set_alpha(255)
        screen.blit(self.logo_chuakz, (15, 15))

        self.logo_img.set_alpha(255)
        screen.blit(self.logo_img, (494, 173))

        self.info_btn.render(screen)
        self.play_btn.render(screen)
        self.about_btn.render(screen)
        self.exit_btn.render(screen)


def change_menu(menu: dict, crnt_page: str, screen):
    # Main Menu Page
    if crnt_page == "main_menu":
        if menu["main_menu"].play_btn.check(pygame.mouse.get_pos()):
            Menu.click_sound.play()
            menu["play_menu"].render(screen)
            return "play_menu"

        if menu["main_menu"].about_btn.check(pygame.mouse.get_pos()):
            Menu.click_sound.play()
            menu["about_menu"].render(screen)
            return "about_menu"

        if menu["main_menu"].exit_btn.check(pygame.mouse.get_pos()):
            Menu.click_sound.play()
            return "<exit>"

    # About Menu
    elif crnt_page == "about_menu":
        if menu["about_menu"].back_btn.check(pygame.mouse.get_pos()):
            Menu.click_sound.play()
            menu["main_menu"].render(screen)
            return "main_menu"

    # # Info Menu
    # elif crnt_page == "info_menu":
    #     if menu["info_menu"].back_btn.check(pygame.mouse.get_pos()):
    #         Menu.click_sound.play()
    #         menu["main_menu"].render(screen)
    #         return "main_menu"

    # Else return default state
    return crnt_page
