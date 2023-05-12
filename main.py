# Modul Utama
import pygame
import sys

# Inisiasi PYGAME
pygame.init()
fps_clock = pygame.time.Clock()

# Pengaturan
SIZE = (1280, 720)
icon = pygame.image.load("assets/images/icon.png")
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Lost")
pygame.display.set_icon(icon)


def main():
    # game = Game(screen, fps_clock)
    pygame.quit()


if __name__ == "__main__":
    main()
