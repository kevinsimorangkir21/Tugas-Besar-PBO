import pygame
import random
import button
import asset
import Enemy_Hero

pygame.init()

damage_text_group = Enemy_Hero.damage_text_group
asset = asset.Game()
#level1 dan 2
knight = Enemy_Hero.knight
bandit1 = Enemy_Hero.bandit1
bandit2 = Enemy_Hero.bandit2
bandit3 = Enemy_Hero.bandit3

#level1
bandit_list = []
bandit_list.append(bandit1)
bandit_list.append(bandit2)

#level1 dan 2
knight_health_bar = Enemy_Hero.ConcreteHealthBar(100, Enemy_Hero.screen_height - Enemy_Hero.bottom_panel + 40, knight.hp, knight.max_hp)
bandit1_health_bar = Enemy_Hero.ConcreteHealthBar(550, Enemy_Hero.screen_height - Enemy_Hero.bottom_panel + 40, bandit1.hp, bandit1.max_hp)
bandit2_health_bar = Enemy_Hero.ConcreteHealthBar(550, Enemy_Hero.screen_height - Enemy_Hero.bottom_panel + 100, bandit2.hp, bandit2.max_hp)
bandit3_health_bar = Enemy_Hero.ConcreteHealthBar(550, Enemy_Hero.screen_height - Enemy_Hero.bottom_panel + 10, bandit2.hp, bandit2.max_hp)

#level2
bandit_list2 = []
bandit_list2.append(bandit1)
bandit_list2.append(bandit2)
bandit_list2.append(bandit3)

#create buttons
potion_button = button.Button(Enemy_Hero.screen, 100, Enemy_Hero.screen_height - Enemy_Hero.bottom_panel + 70, asset.potion_img, 64, 64)
restart_button = button.Button(Enemy_Hero.screen, 330, 120, asset.restart_img, 120, 30)
level_2_button = button.Button(Enemy_Hero.screen, 450, 120, asset.level2_img, 120, 30)

asset.backsound.play(-1)
volume_value = 0.3
asset.backsound.set_volume(volume_value)

level_1 = True
level_2 = False
level_3 = False
run = True
while run:
	Enemy_Hero.clock.tick(Enemy_Hero.fps)
	#draw background

	if level_1:
		Enemy_Hero.Display.draw_bg()
		#draw panel
		Enemy_Hero.Display.draw_panel()
		knight_health_bar.draw(knight.hp)
		bandit1_health_bar.draw(bandit1.hp)
		bandit2_health_bar.draw(bandit2.hp)


		#draw fighters
		knight.update()
		knight.draw()
		for bandit in bandit_list:
			bandit.update()
			bandit.draw()

		#draw the damage text
		damage_text_group.update()
		damage_text_group.draw(Enemy_Hero.screen)

		#control player actions
		#reset action variables
		asset.attack = False
		asset.potion = False
		target = None
		#make sure mouse is visible
		pygame.mouse.set_visible(True)
		pos = pygame.mouse.get_pos()
		for count, bandit in enumerate(bandit_list):
			if bandit.rect.collidepoint(pos):
				#hide mouse
				pygame.mouse.set_visible(False)
				#show sword in place of mouse cursor
				Enemy_Hero.screen.blit(asset.sword_img, pos)
				if asset.clicked == True and bandit.alive == True:
					asset.attack = True
					target = bandit_list[count]
		if potion_button.draw():
			asset.potion = True
		#show number of potions remaining
		Enemy_Hero.Display.draw_text(str(knight.potions), asset.font, asset.red, 150, Enemy_Hero.screen_height - Enemy_Hero.bottom_panel + 70)


		if asset.game_over == 0:
			#player action
			if knight.alive == True:
				if asset.current_fighter == 1:
					asset.action_cooldown += 1
					if asset.action_cooldown >= asset.action_wait_time:
						#look for player action
						#attack
						if asset.attack == True and target != None:
							knight.attack(target)
							asset.current_fighter += 1
							asset.action_cooldown = 0
						#potion
						if asset.potion == True:
							if knight.potions > 0:
								#check if the potion would heal the player beyond max health
								if knight.max_hp - knight.hp > asset.potion_effect:
									heal_amount = asset.potion_effect
								else:
									heal_amount = knight.max_hp - knight.hp
								knight.hp += heal_amount
								knight.potions -= 1
								damage_text = Enemy_Hero.DamageText(knight.rect.centerx, knight.rect.y, str(heal_amount), asset.green)
								damage_text_group.add(damage_text)
								asset.healup.play()
								asset.current_fighter += 1
								asset.action_cooldown = 0
			else:
				asset.game_over = -1


			#enemy action
			for count, bandit in enumerate(bandit_list):
				if asset.current_fighter == 2 + count:
					if bandit.alive == True:
						asset.action_cooldown += 1
						if asset.action_cooldown >= asset.action_wait_time:
							#check if bandit needs to heal first
							if (bandit.hp / bandit.max_hp) < 0.5 and bandit.potions > 0:
								#check if the potion would heal the bandit beyond max health
								if bandit.max_hp - bandit.hp > asset.potion_effect:
									heal_amount = asset.potion_effect
								else:
									heal_amount = bandit.max_hp - bandit.hp
								bandit.hp += heal_amount
								bandit.potions -= 1
								damage_text = Enemy_Hero.DamageText(bandit.rect.centerx, bandit.rect.y, str(heal_amount), asset.green)
								damage_text_group.add(damage_text)
								asset.healup.play()
								asset.current_fighter += 1
								asset.action_cooldown = 0
							#attack
							else:
								bandit.attack(knight)
		
								asset.current_fighter += 1
								asset.action_cooldown = 0
					else:
						asset.current_fighter += 1

			#if all fighters have had a turn then reset
			if asset.current_fighter > asset.total_fighters:
				asset.current_fighter = 1


		#check if all bandits are dead
		alive_bandits = 0
		for bandit in bandit_list:
			if bandit.alive == True:
				alive_bandits += 1
		if alive_bandits == 0:
			asset.game_over = 1


		#check if game is over
		if asset.game_over != 0:
			if asset.game_over == 1:
				Enemy_Hero.screen.blit(asset.victory_img, (250, 50))
				if restart_button.draw():
					knight.reset()
					for bandit in bandit_list:
						bandit.reset()
					asset.current_fighter = 1
					asset.action_cooldown
					asset.game_over = 0
					level_1 = True
					level_2 = False
				if level_2_button.draw():
					level_1 = False
					level_2 = True
					knight.reset()
					for bandit in bandit_list2:
						bandit.reset()
					asset.current_fighter = 1
					asset.action_cooldown
					asset.game_over = 0					
			if asset.game_over == -1:
				Enemy_Hero.screen.blit(asset.defeat_img, (290, 50))
				if restart_button.draw():
					knight.reset()
					for bandit in bandit_list:
						bandit.reset()
					asset.current_fighter = 1
					asset.action_cooldown
					asset.game_over = 0	

	elif level_2:
		Enemy_Hero.Display.draw_bg()
		#draw panel
		Enemy_Hero.Display.draw_panel_2()
		knight_health_bar.draw(knight.hp)
		bandit1_health_bar.draw(bandit1.hp)
		bandit2_health_bar.draw(bandit2.hp)
		bandit3_health_bar.draw(bandit3.hp)
		#draw fighters
		knight.update()
		knight.draw()
		for bandit in bandit_list2:
			bandit.update()
			bandit.draw()

		#draw the damage text
		damage_text_group.update()
		damage_text_group.draw(Enemy_Hero.screen)

		#control player actions
		#reset action variables
		asset.attack = False
		asset.potion = False
		target = None
		#make sure mouse is visible
		pygame.mouse.set_visible(True)
		pos = pygame.mouse.get_pos()
		for count, bandit in enumerate(bandit_list2):
			if bandit.rect.collidepoint(pos):
				#hide mouse
				pygame.mouse.set_visible(False)
				#show sword in place of mouse cursor
				Enemy_Hero.screen.blit(asset.sword_img, pos)
				if asset.clicked == True and bandit.alive == True:
					asset.attack = True
					target = bandit_list2[count]
		if potion_button.draw():
			asset.potion = True
		#show number of potions remaining
		Enemy_Hero.Display.draw_text(str(knight.potions), asset.font, asset.red, 150, Enemy_Hero.screen_height - Enemy_Hero.bottom_panel + 70)


		if asset.game_over == 0:
			#player action
			if knight.alive == True:
				if asset.current_fighter == 1:
					asset.action_cooldown += 1
					if asset.action_cooldown >= asset.action_wait_time:
						#look for player action
						#attack
						if asset.attack == True and target != None:
							knight.attack(target)
							asset.current_fighter += 1
							asset.action_cooldown = 0
						#potion
						if asset.potion == True:
							if knight.potions > 0:
								#check if the potion would heal the player beyond max health
								if knight.max_hp - knight.hp > asset.potion_effect:
									heal_amount = asset.potion_effect
								else:
									heal_amount = knight.max_hp - knight.hp
								knight.hp += heal_amount
								knight.potions -= 1
								damage_text = Enemy_Hero.DamageText(knight.rect.centerx, knight.rect.y, str(heal_amount), asset.green)
								damage_text_group.add(damage_text)
								asset.healup.play()
								asset.current_fighter += 1
								asset.action_cooldown = 0
			else:
				asset.game_over = -1


			#enemy action
			for count, bandit in enumerate(bandit_list2):
				if asset.current_fighter == 2 + count:
					if bandit.alive == True:
						asset.action_cooldown += 1
						if asset.action_cooldown >= asset.action_wait_time:
							#check if bandit needs to heal first
							if (bandit.hp / bandit.max_hp) < 0.5 and bandit.potions > 0:
								#check if the potion would heal the bandit beyond max health
								if bandit.max_hp - bandit.hp > asset.potion_effect:
									heal_amount = asset.potion_effect
								else:
									heal_amount = bandit.max_hp - bandit.hp
								bandit.hp += heal_amount
								bandit.potions -= 1
								damage_text = Enemy_Hero.DamageText(bandit.rect.centerx, bandit.rect.y, str(heal_amount), asset.green)
								damage_text_group.add(damage_text)
								asset.healup.play()
								asset.current_fighter += 1
								asset.action_cooldown = 0
							#attack
							else:
								bandit.attack(knight)
		
								asset.current_fighter += 1
								asset.action_cooldown = 0
					else:
						asset.current_fighter += 1

			#if all fighters have had a turn then reset
			if asset.current_fighter > asset.total_fighters:
				asset.current_fighter = 1


		#check if all bandits are dead
		alive_bandits = 0
		for bandit in bandit_list2:
			if bandit.alive == True:
				alive_bandits += 1
		if alive_bandits == 0:
			asset.game_over = 1


		#check if game is over
		if asset.game_over != 0:
			if asset.game_over == 1:
				Enemy_Hero.screen.blit(asset.victory_img, (250, 50))
				if restart_button.draw():
					knight.reset()
					for bandit in bandit_list:
						bandit.reset()
					asset.current_fighter = 1
					asset.action_cooldown
					asset.game_over = 0
					level_1 = True
					level_2 = False				
			if asset.game_over == -1:
				Enemy_Hero.screen.blit(asset.defeat_img, (290, 50))
				if restart_button.draw():
					knight.reset()
					for bandit in bandit_list2:
						bandit.reset()
					asset.current_fighter = 1
					asset.action_cooldown
					asset.game_over = 0	

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
		if event.type == pygame.MOUSEBUTTONDOWN:
			asset.clicked = True
		else:
			asset.clicked = False

	pygame.display.update()

pygame.quit()