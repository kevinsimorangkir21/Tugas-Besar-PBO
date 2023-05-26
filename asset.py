import pygame

class Game:
    def __init__(self):

        # Game variables
        self.current_fighter = 1
        self.total_fighters_on_3_enemy = 4
        self.total_fighters_on_2_enemy = 3
        self.total_fighters_on_1_enemy = 2 
        self.action_cooldown = 0
        self.action_wait_time = 90
        self.attack = False
        self.potion = False
        self.potion_effect = 15
        self.clicked = False
        self.game_over = 0
        self.start = False

        # Define fonts
        self.font = pygame.font.SysFont('Times New Roman', 26)

        # Define colors
        self.red = (255, 0, 0)
        self.green = (0, 255, 0)

        # Load images
        # Background image
        self.background_img = pygame.image.load('img/Background/background.png').convert_alpha()
        self.background2_img = pygame.image.load('img/Background/background2.png').convert_alpha()
        # Panel image
        self.panel_img = pygame.image.load('img/Icons/panel.png').convert_alpha()
        # Button images
        self.potion_img = pygame.image.load('img/Icons/potion.png').convert_alpha()
        self.restart_img = pygame.image.load('img/Icons/restart.png').convert_alpha()
        self.level2_img = pygame.image.load('img/Icons/level_2.png').convert_alpha()
        self.level3_img = pygame.image.load('img/Icons/level_3.png').convert_alpha()
        self.level4_img = pygame.image.load('img/Icons/level_4.png').convert_alpha()
        self.level5_img = pygame.image.load('img/Icons/level_5.png').convert_alpha()
        self.level6_img = pygame.image.load('img/Icons/level_6.png').convert_alpha()
        self.cchoose_img = pygame.image.load('img/Icons/choose.png').convert_alpha()
        self.knightbutton_img = pygame.image.load('img/Icons/Knights.png').convert_alpha()
        self.nightbornebutton_img = pygame.image.load('img/Icons/nightborne.png').convert_alpha()
        # Load victory and defeat images
        self.victory_img = pygame.image.load('img/Icons/victory.png').convert_alpha()
        self.defeat_img = pygame.image.load('img/Icons/defeat.png').convert_alpha()
        # Sword image
        self.sword_img = pygame.image.load('img/Icons/sword.png').convert_alpha()
        # main sound       
        self.backsound = pygame.mixer.Sound('sound\ssound.mp3')
        self.healup = pygame.mixer.Sound('sound\heal-up.wav')
        #bandit sound
        self.gethurt_bandit = pygame.mixer.Sound('sound\ibandit\hurtbandit.wav')
        self.attackbandit_sound = pygame.mixer.Sound('sound\ibandit\serangbandit.wav')
        self.death_bandit = pygame.mixer.Sound('sound\ibandit\matibandit1.wav')
        #knight sound
        self.death_knight = pygame.mixer.Sound('sound\knight\matiknight1.wav')
        self.gethurt_knight = pygame.mixer.Sound('sound\knight\knighthurt.wav')
        self.attackknight_sound = pygame.mixer.Sound('sound\knight\knightattack.wav')
        #siren sound
        self.attacksirensword_sound = pygame.mixer.Sound('sound\siren\sirenswordsound.wav')
        self.attacksirenvoice_sound = pygame.mixer.Sound('sound\siren\serangsiren.wav')
        self.deathsiren_sound = pygame.mixer.Sound('sound\siren\matisiren.wav')
        self.hurtsiren_sound = pygame.mixer.Sound('sound\siren\hurtsiren.wav')
        #wizard sound
        self.wizardattack_sound =  pygame.mixer.Sound('sound\wizard\wizardattack.wav')
        self.wizarddeath_sound =  pygame.mixer.Sound('sound\wizard\wizarddeath.wav')
        self.wizardhurt_sound =  pygame.mixer.Sound('sound\wizard\wizardhurt.wav')
        #bossmonstersound
        self.monsterattack_sound = pygame.mixer.Sound('sound\monster\monsterattack.wav')
        self.monsterdeath_sound = pygame.mixer.Sound('sound\monster\monsterdeath.wav')
        self.monsterhurt_sound = pygame.mixer.Sound('sound\monster\monsterhurt.wav')
        #nightbornesound
        self.nightborneattack_sound = pygame.mixer.Sound('sound\inightborne\inightborneattack.wav')
        self.nightborneattacksword_sound = pygame.mixer.Sound('sound\inightborne\inightborneattacksword1.wav')
        self.nightbornedeath_sound = pygame.mixer.Sound('sound\inightborne\inightbornedeath.wav')
        self.nightbornehurt_sound = pygame.mixer.Sound('sound\inightborne\inightbornehurt.wav')
        self.nightborneexplosion_sound = pygame.mixer.Sound('sound\inightborne\inightborneexplosion.wav')