import pygame

class Game:
    def __init__(self):

        # Game variables
        self.current_fighter = 1
        self.total_fighters = 3
        self.action_cooldown = 0
        self.action_wait_time = 90
        self.attack = False
        self.potion = False
        self.potion_effect = 15
        self.clicked = False
        self.game_over = 0

        # Define fonts
        self.font = pygame.font.SysFont('Times New Roman', 26)

        # Define colors
        self.red = (255, 0, 0)
        self.green = (0, 255, 0)

        # Load images
        # Background image
        self.background_img = pygame.image.load('img/Background/background.png').convert_alpha()
        # Panel image
        self.panel_img = pygame.image.load('img/Icons/panel.png').convert_alpha()
        # Button images
        self.potion_img = pygame.image.load('img/Icons/potion.png').convert_alpha()
        self.restart_img = pygame.image.load('img/Icons/restart.png').convert_alpha()
        # Load victory and defeat images
        self.victory_img = pygame.image.load('img/Icons/victory.png').convert_alpha()
        self.defeat_img = pygame.image.load('img/Icons/defeat.png').convert_alpha()
        # Sword image
        self.sword_img = pygame.image.load('img/Icons/sword.png').convert_alpha()
        self.attackknight_sound = pygame.mixer.Sound('sound\swinging-staff-whoosh-strong-08-44658.wav')
        self.attackbandit_sound = pygame.mixer.Sound('sound\mixkit-dagger-woosh-1487.wav')
        self.gethurt_knight = pygame.mixer.Sound('sound\Studio_Project_V1.wav')
        self.backsound = pygame.mixer.Sound('sound\inibacksound.wav')
        self.healup = pygame.mixer.Sound('sound\heal-up.wav')
        self.gethurt_bandit = pygame.mixer.Sound('sound\suarabandit.wav')
        self.death_bandit = pygame.mixer.Sound('sound\matibandit1.wav')
        self.death_knight = pygame.mixer.Sound('sound\matiknight1.wav')