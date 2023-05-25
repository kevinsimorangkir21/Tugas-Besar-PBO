import pygame
import random
import button
import asset
from abc import ABC, abstractmethod

pygame.init()

clock = pygame.time.Clock()
fps = 60

#game window
bottom_panel = 150
screen_width = 800
screen_height = 400 + bottom_panel

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('L0st')

class Display:
	#create function for drawing text
	def draw_text(text, font, text_col, x, y):
		img = font.render(text, True, text_col)
		screen.blit(img, (x, y))


	#function for drawing background
	def draw_bg():
		screen.blit(asset.background_img, (0, 0))


	#function for drawing panel
	def draw_panel():
		#draw panel rectangle
		screen.blit(asset.panel_img, (0, screen_height - bottom_panel))
		#show knight stats
		Display.draw_text(f'{knight.name} HP: {knight.hp}', asset.font, asset.red, 100, screen_height - bottom_panel + 10)
		for count, i in enumerate(bandit_list):
			#show name and health
			Display.draw_text(f'{i.name} HP: {i.hp}', asset.font, asset.red, 550, (screen_height - bottom_panel + 10) + count * 40)

	def draw_panel_2():
		#draw panel rectangle
		screen.blit(asset.panel_img, (0, screen_height - bottom_panel))
		#show knight stats
		Display.draw_text(f'{knight.name} HP: {knight.hp}', asset.font, asset.red, 100, screen_height - bottom_panel + 10)
		for count, i in enumerate(bandit_list2):
			#show name and health
			Display.draw_text(f'{i.name} HP: {i.hp}', asset.font, asset.red, 550, (screen_height - bottom_panel + 10) + count * 40)
	def draw_panel_3():
		#draw panel rectangle
		screen.blit(asset.panel_img, (0, screen_height - bottom_panel))
		#show knight stats
		Display.draw_text(f'{knight.name} HP: {knight.hp}', asset.font, asset.red, 100, screen_height - bottom_panel + 10)
		for count, i in enumerate(siren_list):
			#show name and health
			Display.draw_text(f'{i.name} HP: {i.hp}', asset.font, asset.red, 550, (screen_height - bottom_panel + 10) + count * 40)
	def draw_panel_4():
		#draw panel rectangle
		screen.blit(asset.panel_img, (0, screen_height - bottom_panel))
		#show knight stats
		Display.draw_text(f'{knight.name} HP: {knight.hp}', asset.font, asset.red, 100, screen_height - bottom_panel + 10)
		for count, i in enumerate(wizard_list):
			#show name and health
			Display.draw_text(f'{i.name} HP: {i.hp}', asset.font, asset.red, 550, (screen_height - bottom_panel + 10) + count * 40)

	def draw_panel_6():
		#draw panel rectangle
		screen.blit(asset.panel_img, (0, screen_height - bottom_panel))
		#show knight stats
		Display.draw_text(f'{knight.name} HP: {knight.hp}', asset.font, asset.red, 100, screen_height - bottom_panel + 10)
		for count, i in enumerate(monster_list):
			#show name and health
			Display.draw_text(f'{i.name} HP: {i.hp}', asset.font, asset.red, 550, (screen_height - bottom_panel + 10) + count * 40)

#fighter class
class Fighter():
	def __init__(self, x, y, name, max_hp, strength, potions):
		self.name = name
		self.max_hp = max_hp
		self.hp = max_hp
		self.strength = strength
		self.start_potions = potions
		self.potions = potions
		self.alive = True
		self.animation_list = []
		self.frame_index = 0
		self.action = 0  # 0:idle, 1:attack, 2:hurt, 3:dead
		self.update_time = pygame.time.get_ticks()
		# load idle images
		temp_list = []
		for i in range(8):
			img = pygame.image.load(f'img/{self.name}/Idle/{i}.png')
			img = pygame.transform.scale(img, (img.get_width() * 3, img.get_height() * 3))
			temp_list.append(img)
		self.animation_list.append(temp_list)
		# load attack images
		temp_list = []
		for i in range(8):
			img = pygame.image.load(f'img/{self.name}/Attack/{i}.png')
			img = pygame.transform.scale(img, (img.get_width() * 3, img.get_height() * 3))
			temp_list.append(img)
		self.animation_list.append(temp_list)
		# load hurt images
		temp_list = []
		for i in range(3):
			img = pygame.image.load(f'img/{self.name}/Hurt/{i}.png')
			img = pygame.transform.scale(img, (img.get_width() * 3, img.get_height() * 3))
			temp_list.append(img)
		self.animation_list.append(temp_list)
		# load death images
		temp_list = []
		for i in range(10):
			img = pygame.image.load(f'img/{self.name}/Death/{i}.png')
			img = pygame.transform.scale(img, (img.get_width() * 3, img.get_height() * 3))
			temp_list.append(img)
		self.animation_list.append(temp_list)
		self.image = self.animation_list[self.action][self.frame_index]
		self.rect = self.image.get_rect()
		self.rect.center = (x, y)

	def update(self):
		animation_cooldown = 100
		# handle animation
		# update image
		self.image = self.animation_list[self.action][self.frame_index]
		# check if enough time has passed since the last update
		if pygame.time.get_ticks() - self.update_time > animation_cooldown:
			self.update_time = pygame.time.get_ticks()
			self.frame_index += 1
		# if the animation has run out then reset back to the start
		if self.frame_index >= len(self.animation_list[self.action]):
			if self.action == 3:
				self.frame_index = len(self.animation_list[self.action]) - 1
			else:
				self.idle()

	def idle(self):
		# set variables to idle animation
		self.action = 0
		self.frame_index = 0
		self.update_time = pygame.time.get_ticks()

	def draw(self):
		screen.blit(self.image, self.rect)


class Bandit(Fighter):
	def __init__(self, x, y, name, max_hp, strength, potions):
		super().__init__(x, y, name, max_hp, strength, potions)
        

	def attack(self, target):
		# deal damage to enemy
		rand = random.randint(-5, 5)
		damage = self.strength + rand
		target.hp -= damage
		# run enemy hurt animation
		target.hurt()
		asset.attackbandit_sound.play()
		# check if target has died
		if target.hp < 1:
			target.hp = 0
			target.alive = False
			target.death()
		damage_text = DamageText(target.rect.centerx, target.rect.y, str(damage), asset.red)
		damage_text_group.add(damage_text)
		# set variables to attack animation
		self.action = 1
		self.frame_index = 0
		self.update_time = pygame.time.get_ticks()

	def hurt(self):
		# set variables to hurt animation
		self.action = 2
		asset.gethurt_bandit.play()
		self.frame_index = 0
		self.update_time = pygame.time.get_ticks()

	def death(self):
		# set variables to death animation
		self.action = 3
		asset.death_bandit.play()
		self.frame_index = 0
		self.update_time = pygame.time.get_ticks()
		
	def reset(self):
		self.alive = True
		self.potions = self.start_potions
		self.hp = self.max_hp
		self.frame_index = 0
		self.action = 0
		self.update_time = pygame.time.get_ticks()


class Knight(Fighter):
	def __init__(self, x, y, name, max_hp, strength, potions):
		super().__init__(x, y, name, max_hp, strength, potions)
	

	def attack(self, target):
		asset.attackknight_sound.play()
		
		# deal damage to enemy
		rand = random.randint(-5, 5)
		damage = self.strength + rand
		target.hp -= damage
		# run enemy hurt animation
		target.hurt()

		# check if target has died
		if target.hp < 1:
			target.hp = 0
			target.alive = False
			target.death()
		damage_text = DamageText(target.rect.centerx, target.rect.y, str(damage), asset.red)
		damage_text_group.add(damage_text)
		# set variables to attack animation
		self.action = 1
		self.frame_index = 0
		self.update_time = pygame.time.get_ticks()

	def hurt(self):
		# set variables to hurt animation
		self.action = 2
		asset.gethurt_knight.play()
		self.frame_index = 0
		self.update_time = pygame.time.get_ticks()

	def death(self):
		# set variables to death animation
		self.action = 3
		asset.death_knight.play()
		self.frame_index = 0
		self.update_time = pygame.time.get_ticks()

	def reset(self):
		self.alive = True
		self.potions = self.start_potions
		self.hp = self.max_hp
		self.frame_index = 0
		self.action = 0
		self.update_time = pygame.time.get_ticks()

class Siren(Fighter):
	def __init__(self, x, y, name, max_hp, strength, potions):
		super().__init__(x, y, name, max_hp, strength, potions)
	

	def attack(self, target):
		asset.attacksirensword_sound.play()
		asset.attacksirenvoice_sound.play()
		
		# deal damage to enemy
		rand = random.randint(-5, 10)
		damage = self.strength + rand
		target.hp -= damage
		# run enemy hurt animation
		target.hurt()

		# check if target has died
		if target.hp < 1:
			target.hp = 0
			target.alive = False
			target.death()
		damage_text = DamageText(target.rect.centerx, target.rect.y, str(damage), asset.red)
		damage_text_group.add(damage_text)
		# set variables to attack animation
		self.action = 1
		self.frame_index = 0
		self.update_time = pygame.time.get_ticks()

	def hurt(self):
		# set variables to hurt animation
		self.action = 2
		asset.hurtsiren_sound.play()
		self.frame_index = 0
		self.update_time = pygame.time.get_ticks()

	def death(self):
		# set variables to death animation
		self.action = 3
		asset.deathsiren_sound.play()
		self.frame_index = 0
		self.update_time = pygame.time.get_ticks()

	def reset(self):
		self.alive = True
		self.potions = self.start_potions
		self.hp = self.max_hp
		self.frame_index = 0
		self.action = 0
		self.update_time = pygame.time.get_ticks()

class Wizard(Fighter):
	def __init__(self, x, y, name, max_hp, strength, potions):
		super().__init__(x, y, name, max_hp, strength, potions)
	

	def attack(self, target):
		asset.wizardattack_sound.play()

		# deal damage to enemy
		rand = random.randint(-5, 10)
		damage = self.strength + rand
		target.hp -= damage
		# run enemy hurt animation
		target.hurt()

		# check if target has died
		if target.hp < 1:
			target.hp = 0
			target.alive = False
			target.death()
		damage_text = DamageText(target.rect.centerx, target.rect.y, str(damage), asset.red)
		damage_text_group.add(damage_text)
		# set variables to attack animation
		self.action = 1
		self.frame_index = 0
		self.update_time = pygame.time.get_ticks()

	def hurt(self):
		# set variables to hurt animation
		self.action = 2
		asset.wizardhurt_sound.play()
		self.frame_index = 0
		self.update_time = pygame.time.get_ticks()

	def death(self):
		# set variables to death animation
		self.action = 3
		asset.wizarddeath_sound.play()
		self.frame_index = 0
		self.update_time = pygame.time.get_ticks()

	def reset(self):
		self.alive = True
		self.potions = self.start_potions
		self.hp = self.max_hp
		self.frame_index = 0
		self.action = 0
		self.update_time = pygame.time.get_ticks()

class Monster(Fighter):
	def __init__(self, x, y, name, max_hp, strength, potions):
		super().__init__(x, y, name, max_hp, strength, potions)
	

	def attack(self, target):
		asset.monsterattack_sound.play()

		# deal damage to enemy
		rand = random.randint(-5, 10)
		damage = self.strength + rand
		target.hp -= damage
		# run enemy hurt animation
		target.hurt()

		# check if target has died
		if target.hp < 1:
			target.hp = 0
			target.alive = False
			target.death()
		damage_text = DamageText(target.rect.centerx, target.rect.y, str(damage), asset.red)
		damage_text_group.add(damage_text)
		# set variables to attack animation
		self.action = 1
		self.frame_index = 0
		self.update_time = pygame.time.get_ticks()

	def hurt(self):
		# set variables to hurt animation
		self.action = 2
		asset.monsterhurt_sound.play()
		self.frame_index = 0
		self.update_time = pygame.time.get_ticks()

	def death(self):
		# set variables to death animation
		self.action = 3
		asset.monsterdeath_sound.play()
		self.frame_index = 0
		self.update_time = pygame.time.get_ticks()

	def reset(self):
		self.alive = True
		self.potions = self.start_potions
		self.hp = self.max_hp
		self.frame_index = 0
		self.action = 0
		self.update_time = pygame.time.get_ticks()

class HealthBar(ABC):
	def __init__(self, x, y, hp, max_hp):
		self.x = x
		self.y = y
		self.hp = hp
		self.max_hp = max_hp

	@abstractmethod
	def draw(self, hp):
		pass


class ConcreteHealthBar(HealthBar):
	def draw(self, hp):
		# update with new health
		self.hp = hp
		# calculate health ratio
		ratio = self.hp / self.max_hp
		pygame.draw.rect(screen, asset.red, (self.x, self.y, 150, 10))
		pygame.draw.rect(screen, asset.green, (self.x, self.y, 150 * ratio, 10))


class DamageText(pygame.sprite.Sprite):
	def __init__(self, x, y, damage, colour):
		pygame.sprite.Sprite.__init__(self)
		self.image = asset.font.render(damage, True, colour)
		self.rect = self.image.get_rect()
		self.rect.center = (x, y)
		self.counter = 0

	def update(self):
		# move damage text up
		self.rect.y -= 1
		# delete the text after a few seconds
		self.counter += 1
		if self.counter > 30:
			self.kill()




damage_text_group = pygame.sprite.Group()

asset = asset.Game()
#level 1 dan 2
knight = Knight(200, 260, 'Knight', 30, 10, 3)
bandit1 = Bandit(550, 270, 'Bandit', 2, 6, 1)
bandit2 = Bandit(700, 270, 'Bandit', 1, 6, 1)
bandit3 = Bandit(400, 270, 'Bandit', 1, 6, 1)


bandit_list = []
bandit_list.append(bandit1)
bandit_list.append(bandit2)

#level2
bandit_list2 = []
bandit_list2.append(bandit1)
bandit_list2.append(bandit2)
bandit_list2.append(bandit3)

#level3
siren1 = Siren(550, 270, 'Siren', 8, 8, 2)
siren2 = Siren(700, 270, 'Siren', 8, 8, 2)
siren_list = []
siren_list.append(siren1)
siren_list.append(siren2)

#level4
wizard1 = Wizard(550, 255, 'Wizard', 8, 8, 2)
wizard2 = Wizard(700, 255, 'Wizard', 8, 8, 2)
wizard_list = []
wizard_list.append(wizard1)
wizard_list.append(wizard2)

#Level6
monster1 = Monster(10, 25, 'Monster', 8, 8, 2)
monster_list = []
monster_list.append(monster1)
