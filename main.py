#Menu Import File
import pygame
import random
import button
import asset
import Enemy_Hero

pygame.init()
 
damage_text_group = Enemy_Hero.damage_text_group
asset = asset.Game()

#select char
char_knight = Enemy_Hero.knight_select
char_nightborne = Enemy_Hero.nightborne_select

#level1 dan 2
knight = Enemy_Hero.knight
nightborne = Enemy_Hero.nightborne
bandit1 = Enemy_Hero.bandit1
bandit2 = Enemy_Hero.bandit2
bandit3 = Enemy_Hero.bandit3

#level1
bandit_list = []
bandit_list.append(bandit1)
bandit_list.append(bandit2)

#level1 dan 2
knight_health_bar = Enemy_Hero.ConcreteHealthBar(100, Enemy_Hero.screen_height - Enemy_Hero.bottom_panel + 40, knight.hp, knight.max_hp)
nightborne_health_bar = Enemy_Hero.ConcreteHealthBar(100, Enemy_Hero.screen_height - Enemy_Hero.bottom_panel + 40, nightborne.hp, nightborne.max_hp)
bandit1_health_bar = Enemy_Hero.ConcreteHealthBar(550, Enemy_Hero.screen_height - Enemy_Hero.bottom_panel + 40, bandit1.hp, bandit1.max_hp)
bandit2_health_bar = Enemy_Hero.ConcreteHealthBar(550, Enemy_Hero.screen_height - Enemy_Hero.bottom_panel + 80, bandit2.hp, bandit2.max_hp)
bandit3_health_bar = Enemy_Hero.ConcreteHealthBar(550, Enemy_Hero.screen_height - Enemy_Hero.bottom_panel + 120, bandit3.hp, bandit3.max_hp)

#level2
bandit_list2 = []
bandit_list2.append(bandit1)
bandit_list2.append(bandit2)
bandit_list2.append(bandit3)

#level3
siren1 = Enemy_Hero.siren1
siren2 = Enemy_Hero.siren2
siren_list = []
siren_list.append(siren1)
siren_list.append(siren2)
siren1_health_bar = Enemy_Hero.ConcreteHealthBar(550, Enemy_Hero.screen_height - Enemy_Hero.bottom_panel + 40, siren1.hp, siren1.max_hp)
siren2_health_bar = Enemy_Hero.ConcreteHealthBar(550, Enemy_Hero.screen_height - Enemy_Hero.bottom_panel + 80, siren2.hp, siren2.max_hp)

#level4
wizard1 = Enemy_Hero.wizard1
wizard2 = Enemy_Hero.wizard2
wizard_list = []
wizard_list.append(wizard1)
wizard_list.append(wizard2)
wizard1_health_bar = Enemy_Hero.ConcreteHealthBar(550, Enemy_Hero.screen_height - Enemy_Hero.bottom_panel + 40, wizard1.hp, wizard1.max_hp)
wizard2_health_bar = Enemy_Hero.ConcreteHealthBar(550, Enemy_Hero.screen_height - Enemy_Hero.bottom_panel + 80, wizard2.hp, wizard2.max_hp)

#level5
wizard3 = Enemy_Hero.wizard3
wizard_list2 = []
wizard_list2.append(wizard1)
wizard_list2.append(wizard2)
wizard_list2.append(wizard3)
wizard3_health_bar = Enemy_Hero.ConcreteHealthBar(550, Enemy_Hero.screen_height - Enemy_Hero.bottom_panel + 120, wizard3.hp, wizard3.max_hp)

#level6
monster1 = Enemy_Hero.monster1
monster_list = []
monster_list.append(monster1)
monster1_health_bar = Enemy_Hero.ConcreteHealthBar(550, Enemy_Hero.screen_height - Enemy_Hero.bottom_panel + 40, monster1.hp, monster1.max_hp)


#create buttons
potion_button = button.Button(Enemy_Hero.screen, 100, Enemy_Hero.screen_height - Enemy_Hero.bottom_panel + 70, asset.potion_img, 64, 64)
restart_button = button.Button(Enemy_Hero.screen, 230, 120, asset.restart_img, 120, 30)
level_2_button = button.Button(Enemy_Hero.screen, 430, 120, asset.level2_img, 120, 30)
level_3_button = button.Button(Enemy_Hero.screen, 430, 120, asset.level3_img, 120, 30)
level_4_button = button.Button(Enemy_Hero.screen, 430, 120, asset.level4_img, 120, 30)
level_5_button = button.Button(Enemy_Hero.screen, 430, 120, asset.level5_img, 120, 30)
level_6_button = button.Button(Enemy_Hero.screen, 430, 120, asset.level6_img, 120, 30)
charknight_button = button.Button(Enemy_Hero.screen, 250, 180, asset.knightbutton_img, 120, 30)
charnightborne_button = button.Button(Enemy_Hero.screen, 400, 180, asset.nightbornebutton_img, 120, 30)

asset.backsound.play(-1)
volume_value = 0.35
asset.backsound.set_volume(volume_value)
def character_selection_screen():
	Enemy_Hero.clock.tick(Enemy_Hero.fps)
	Enemy_Hero.Display.draw_bg2()
	Enemy_Hero.screen.blit(asset.cchoose_img, (50, 50))
	char_knight.update()
	char_knight.draw()
	char_nightborne.update()
	char_nightborne.draw()
	if charnightborne_button.draw():
		Enemy_Hero.character = nightborne		
		asset.start = True
	if charknight_button.draw():
		Enemy_Hero.character = knight
		asset.start = True

level_1 = True
level_2 = False
level_3 = False
level_4 = False
level_5 = False
level_6 = False
game_started = False

run = True
while run:
	if not game_started:
		character_selection_screen()
		if asset.start:
			game_started = True	
	
	else:		
		Enemy_Hero.clock.tick(Enemy_Hero.fps)
		#draw background
		if level_1:
			Enemy_Hero.Display.draw_bg()
			#draw panel
			Enemy_Hero.Display.draw_panel()
			if Enemy_Hero.character == nightborne:
				nightborne_health_bar.draw(Enemy_Hero.character.hp)
			else:
				knight_health_bar.draw(Enemy_Hero.character.hp)
			bandit1_health_bar.draw(bandit1.hp)
			bandit2_health_bar.draw(bandit2.hp)


			#draw fighters
			Enemy_Hero.character.update()
			Enemy_Hero.character.draw()
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
			Enemy_Hero.Display.draw_text(str(Enemy_Hero.character.potions), asset.font, asset.red, 150, Enemy_Hero.screen_height - Enemy_Hero.bottom_panel + 70)


			if asset.game_over == 0:
				#player action
				if Enemy_Hero.character.alive == True:
					if asset.current_fighter == 1:
						asset.action_cooldown += 1
						if asset.action_cooldown >= asset.action_wait_time:
							#look for player action
							#attack
							if asset.attack == True and target != None:
								Enemy_Hero.character.attack(target)
								asset.current_fighter += 1
								asset.action_cooldown = 0
							#potion
							if asset.potion == True:
								if Enemy_Hero.character.potions > 0:
									#check if the potion would heal the player beyond max health
									if Enemy_Hero.character.max_hp - Enemy_Hero.character.hp > asset.potion_effect:
										heal_amount = asset.potion_effect
									else:
										heal_amount = Enemy_Hero.character.max_hp - Enemy_Hero.character.hp
									Enemy_Hero.character.hp += heal_amount
									Enemy_Hero.character.potions -= 1
									damage_text = Enemy_Hero.DamageText(Enemy_Hero.character.rect.centerx, Enemy_Hero.character.rect.y, str(heal_amount), asset.green)
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
									bandit.attack(Enemy_Hero.character)
			
									asset.current_fighter += 1
									asset.action_cooldown = 0
						else:
							asset.current_fighter += 1

				#if all fighters have had a turn then reset
				if asset.current_fighter > asset.total_fighters_on_2_enemy:
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
						Enemy_Hero.character.reset()
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
						Enemy_Hero.character.reset()
						for bandit in bandit_list:
							bandit.reset()
						for bandit in bandit_list2:
							bandit.reset()
						asset.current_fighter = 1
						asset.action_cooldown
						asset.game_over = 0					
				if asset.game_over == -1:
					Enemy_Hero.screen.blit(asset.defeat_img, (290, 50))
					if restart_button.draw():
						Enemy_Hero.character.reset()
						for bandit in bandit_list:
							bandit.reset()
						asset.current_fighter = 1
						asset.action_cooldown
						asset.game_over = 0
						level_1 = True	

		elif level_2:
			Enemy_Hero.Display.draw_bg()
			#draw panel
			Enemy_Hero.Display.draw_panel_2()
			if Enemy_Hero.character == nightborne:
				nightborne_health_bar.draw(Enemy_Hero.character.hp)
			else:
				knight_health_bar.draw(Enemy_Hero.character.hp)
			bandit1_health_bar.draw(bandit1.hp)
			bandit2_health_bar.draw(bandit2.hp)
			bandit3_health_bar.draw(bandit3.hp)
			#draw fighters
			Enemy_Hero.character.update()
			Enemy_Hero.character.draw()
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
			Enemy_Hero.Display.draw_text(str(Enemy_Hero.character.potions), asset.font, asset.red, 150, Enemy_Hero.screen_height - Enemy_Hero.bottom_panel + 70)


			if asset.game_over == 0:
				#player action
				if Enemy_Hero.character.alive == True:
					if asset.current_fighter == 1:
						asset.action_cooldown += 1
						if asset.action_cooldown >= asset.action_wait_time:
							#look for player action
							#attack
							if asset.attack == True and target != None:
								Enemy_Hero.character.attack(target)
								asset.current_fighter += 1
								asset.action_cooldown = 0
							#potion
							if asset.potion == True:
								if Enemy_Hero.character.potions > 0:
									#check if the potion would heal the player beyond max health
									if Enemy_Hero.character.max_hp - Enemy_Hero.character.hp > asset.potion_effect:
										heal_amount = asset.potion_effect
									else:
										heal_amount = Enemy_Hero.character.max_hp - Enemy_Hero.character.hp
									Enemy_Hero.character.hp += heal_amount
									Enemy_Hero.character.potions -= 1
									damage_text = Enemy_Hero.DamageText(Enemy_Hero.character.rect.centerx, Enemy_Hero.character.rect.y, str(heal_amount), asset.green)
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
									bandit.attack(Enemy_Hero.character)
			
									asset.current_fighter += 1
									asset.action_cooldown = 0
						else:
							asset.current_fighter += 1

				#if all fighters have had a turn then reset
				if asset.current_fighter > asset.total_fighters_on_3_enemy:
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
						Enemy_Hero.character.reset()
						for bandit in bandit_list2:
							bandit.reset()
						asset.current_fighter = 1
						asset.action_cooldown
						asset.game_over = 0
						level_2 = True
						level_3 = False
					if level_3_button.draw():
						level_2 = False
						level_3 = True
						Enemy_Hero.character.reset()
						for bandit in bandit_list2:
							bandit.reset()
						asset.current_fighter = 1
						asset.action_cooldown
						asset.game_over = 0				
				if asset.game_over == -1:
					Enemy_Hero.screen.blit(asset.defeat_img, (290, 50))
					if restart_button.draw():
						Enemy_Hero.character.reset()
						for bandit in bandit_list2:
							bandit.reset()
						asset.current_fighter = 1
						asset.action_cooldown
						asset.game_over = 0
						level_1 = True

		elif level_3:
			Enemy_Hero.Display.draw_bg()
			#draw panel
			Enemy_Hero.Display.draw_panel_3()
			if Enemy_Hero.character == nightborne:
				nightborne_health_bar.draw(Enemy_Hero.character.hp)
			else:
				knight_health_bar.draw(Enemy_Hero.character.hp)
			siren1_health_bar.draw(siren1.hp)
			siren2_health_bar.draw(siren2.hp)
			
			#draw fighters
			Enemy_Hero.character.update()
			Enemy_Hero.character.draw()
			for siren in siren_list:
				siren.update()
				siren.draw()

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
			for count, siren in enumerate(siren_list):
				if siren.rect.collidepoint(pos):
					#hide mouse
					pygame.mouse.set_visible(False)
					#show sword in place of mouse cursor
					Enemy_Hero.screen.blit(asset.sword_img, pos)
					if asset.clicked == True and siren.alive == True:
						asset.attack = True
						target = siren_list[count]
			if potion_button.draw():
				asset.potion = True
			#show number of potions remaining
			Enemy_Hero.Display.draw_text(str(Enemy_Hero.character.potions), asset.font, asset.red, 150, Enemy_Hero.screen_height - Enemy_Hero.bottom_panel + 70)

			if asset.game_over == 0:
				#player action
				if Enemy_Hero.character.alive == True:
					if asset.current_fighter == 1:
						asset.action_cooldown += 1
						if asset.action_cooldown >= asset.action_wait_time:
							#look for player action
							#attack
							if asset.attack == True and target != None:
								Enemy_Hero.character.attack(target)
								asset.current_fighter += 1
								asset.action_cooldown = 0
							#potion
							if asset.potion == True:
								if Enemy_Hero.character.potions > 0:
									#check if the potion would heal the player beyond max health
									if Enemy_Hero.character.max_hp - Enemy_Hero.character.hp > asset.potion_effect:
										heal_amount = asset.potion_effect
									else:
										heal_amount = Enemy_Hero.character.max_hp - Enemy_Hero.character.hp
									Enemy_Hero.character.hp += heal_amount
									Enemy_Hero.character.potions -= 1
									damage_text = Enemy_Hero.DamageText(Enemy_Hero.character.rect.centerx, Enemy_Hero.character.rect.y, str(heal_amount), asset.green)
									damage_text_group.add(damage_text)
									asset.healup.play()
									asset.current_fighter += 1
									asset.action_cooldown = 0
				else:
					asset.game_over = -1


				#enemy action
				for count, siren in enumerate(siren_list):
					if asset.current_fighter == 2 + count:
						if siren.alive == True:
							asset.action_cooldown += 1
							if asset.action_cooldown >= asset.action_wait_time:
								#check if siren needs to heal first
								if (siren.hp / siren.max_hp) < 0.5 and siren.potions > 0:
									#check if the potion would heal the siren beyond max health
									if siren.max_hp - siren.hp > asset.potion_effect:
										heal_amount = asset.potion_effect
									else:
										heal_amount = siren.max_hp - siren.hp
									siren.hp += heal_amount
									siren.potions -= 1
									damage_text = Enemy_Hero.DamageText(siren.rect.centerx, siren.rect.y, str(heal_amount), asset.green)
									damage_text_group.add(damage_text)
									asset.healup.play()
									asset.current_fighter += 1
									asset.action_cooldown = 0
								#attack
								else:
									siren.attack(Enemy_Hero.character)
			
									asset.current_fighter += 1
									asset.action_cooldown = 0
						else:
							asset.current_fighter += 1

				#if all fighters have had a turn then reset
				if asset.current_fighter > asset.total_fighters_on_2_enemy:
					asset.current_fighter = 1


			#check if all sirens are dead
			alive_siren = 0
			for siren in siren_list:
				if siren.alive == True:
					alive_siren += 1
			if alive_siren == 0:
				asset.game_over = 1


			#check if game is over
			if asset.game_over != 0:
				if asset.game_over == 1:
					Enemy_Hero.screen.blit(asset.victory_img, (250, 50))
					if restart_button.draw():
						Enemy_Hero.character.reset()
						for siren in siren_list:
							siren.reset()
						asset.current_fighter = 1
						asset.action_cooldown
						asset.game_over = 0
						level_3 = True
						level_4 = False	
					if level_4_button.draw():
						level_3 = False
						level_4 = True
						Enemy_Hero.character.reset()
						for siren in siren_list:
							siren.reset()
						asset.current_fighter = 1
						asset.action_cooldown
						asset.game_over = 0		
				if asset.game_over == -1:
					Enemy_Hero.screen.blit(asset.defeat_img, (290, 50))
					if restart_button.draw():
						Enemy_Hero.character.reset()
						for siren in siren_list:
							siren.reset()
						asset.current_fighter = 1
						asset.action_cooldown
						asset.game_over = 0
						level_1 = True			
			
		elif level_4:
			Enemy_Hero.Display.draw_bg()
			#draw panel
			Enemy_Hero.Display.draw_panel_4()
			if Enemy_Hero.character == nightborne:
				nightborne_health_bar.draw(Enemy_Hero.character.hp)
			else:
				knight_health_bar.draw(Enemy_Hero.character.hp)
			wizard1_health_bar.draw(wizard1.hp)
			wizard2_health_bar.draw(wizard2.hp)
			
			#draw fighters
			Enemy_Hero.character.update()
			Enemy_Hero.character.draw()
			for wizard in wizard_list:
				wizard.update()
				wizard.draw()

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
			for count, wizard in enumerate(wizard_list):
				if wizard.rect.collidepoint(pos):
					#hide mouse
					pygame.mouse.set_visible(False)
					#show sword in place of mouse cursor
					Enemy_Hero.screen.blit(asset.sword_img, pos)
					if asset.clicked == True and wizard.alive == True:
						asset.attack = True
						target = wizard_list[count]
			if potion_button.draw():
				asset.potion = True
			#show number of potions remaining
			Enemy_Hero.Display.draw_text(str(Enemy_Hero.character.potions), asset.font, asset.red, 150, Enemy_Hero.screen_height - Enemy_Hero.bottom_panel + 70)


			if asset.game_over == 0:
				#player action
				if Enemy_Hero.character.alive == True:
					if asset.current_fighter == 1:
						asset.action_cooldown += 1
						if asset.action_cooldown >= asset.action_wait_time:
							#look for player action
							#attack
							if asset.attack == True and target != None:
								Enemy_Hero.character.attack(target)
								asset.current_fighter += 1
								asset.action_cooldown = 0
							#potion
							if asset.potion == True:
								if Enemy_Hero.character.potions > 0:
									#check if the potion would heal the player beyond max health
									if Enemy_Hero.character.max_hp - Enemy_Hero.character.hp > asset.potion_effect:
										heal_amount = asset.potion_effect
									else:
										heal_amount = Enemy_Hero.character.max_hp - Enemy_Hero.character.hp
									Enemy_Hero.character.hp += heal_amount
									Enemy_Hero.character.potions -= 1
									damage_text = Enemy_Hero.DamageText(Enemy_Hero.character.rect.centerx, Enemy_Hero.character.rect.y, str(heal_amount), asset.green)
									damage_text_group.add(damage_text)
									asset.healup.play()
									asset.current_fighter += 1
									asset.action_cooldown = 0
				else:
					asset.game_over = -1


				#enemy action
				for count, wizard in enumerate(wizard_list):
					if asset.current_fighter == 2 + count:
						if wizard.alive == True:
							asset.action_cooldown += 1
							if asset.action_cooldown >= asset.action_wait_time:
								#check if wizard needs to heal first
								if (wizard.hp / wizard.max_hp) < 0.5 and wizard.potions > 0:
									#check if the potion would heal the wizard beyond max health
									if wizard.max_hp - wizard.hp > asset.potion_effect:
										heal_amount = asset.potion_effect
									else:
										heal_amount = wizard.max_hp - wizard.hp
									wizard.hp += heal_amount
									wizard.potions -= 1
									damage_text = Enemy_Hero.DamageText(wizard.rect.centerx, wizard.rect.y, str(heal_amount), asset.green)
									damage_text_group.add(damage_text)
									asset.healup.play()
									asset.current_fighter += 1
									asset.action_cooldown = 0
								#attack
								else:
									wizard.attack(Enemy_Hero.character)
			
									asset.current_fighter += 1
									asset.action_cooldown = 0
						else:
							asset.current_fighter += 1

				#if all fighters have had a turn then reset
				if asset.current_fighter > asset.total_fighters_on_2_enemy:
					asset.current_fighter = 1


			#check if all wizard are dead
			alive_wizard = 0
			for wizard in wizard_list:
				if wizard.alive == True:
					alive_wizard += 1
			if alive_wizard == 0:
				asset.game_over = 1


			#check if game is over
			if asset.game_over != 0:
				if asset.game_over == 1:
					Enemy_Hero.screen.blit(asset.victory_img, (250, 50))
					if restart_button.draw():
						Enemy_Hero.character.reset()
						for wizard in wizard_list:
							wizard.reset()
						asset.current_fighter = 1
						asset.action_cooldown
						asset.game_over = 0
						level_4 = True
						level_5 = False	
					if level_5_button.draw():
						level_4 = False
						level_5 = True
						Enemy_Hero.character.reset()
						for wizard in wizard_list:
							wizard.reset()
						asset.current_fighter = 1
						asset.action_cooldown
						asset.game_over = 0		
				if asset.game_over == -1:
					Enemy_Hero.screen.blit(asset.defeat_img, (290, 50))
					if restart_button.draw():
						Enemy_Hero.character.reset()
						for wizard in wizard_list:
							wizard.reset()
						asset.current_fighter = 1
						asset.action_cooldown
						asset.game_over = 0
						level_1 = True
		
		elif level_5:
			Enemy_Hero.Display.draw_bg()
			#draw panel
			Enemy_Hero.Display.draw_panel_5()
			if Enemy_Hero.character == nightborne:
				nightborne_health_bar.draw(Enemy_Hero.character.hp)
			else:
				knight_health_bar.draw(Enemy_Hero.character.hp)
			wizard1_health_bar.draw(wizard1.hp)
			wizard2_health_bar.draw(wizard2.hp)
			wizard3_health_bar.draw(wizard3.hp)
			
			#draw fighters
			Enemy_Hero.character.update()
			Enemy_Hero.character.draw()
			for wizard in wizard_list2:
				wizard.update()
				wizard.draw()

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
			for count, wizard in enumerate(wizard_list2):
				if wizard.rect.collidepoint(pos):
					#hide mouse
					pygame.mouse.set_visible(False)
					#show sword in place of mouse cursor
					Enemy_Hero.screen.blit(asset.sword_img, pos)
					if asset.clicked == True and wizard.alive == True:
						asset.attack = True
						target = wizard_list2[count]
			if potion_button.draw():
				asset.potion = True
			#show number of potions remaining
			Enemy_Hero.Display.draw_text(str(Enemy_Hero.character.potions), asset.font, asset.red, 150, Enemy_Hero.screen_height - Enemy_Hero.bottom_panel + 70)


			if asset.game_over == 0:
				#player action
				if Enemy_Hero.character.alive == True:
					if asset.current_fighter == 1:
						asset.action_cooldown += 1
						if asset.action_cooldown >= asset.action_wait_time:
							#look for player action
							#attack
							if asset.attack == True and target != None:
								Enemy_Hero.character.attack(target)
								asset.current_fighter += 1
								asset.action_cooldown = 0
							#potion
							if asset.potion == True:
								if Enemy_Hero.character.potions > 0:
									#check if the potion would heal the player beyond max health
									if Enemy_Hero.character.max_hp - Enemy_Hero.character.hp > asset.potion_effect:
										heal_amount = asset.potion_effect
									else:
										heal_amount = Enemy_Hero.character.max_hp - Enemy_Hero.character.hp
									Enemy_Hero.character.hp += heal_amount
									Enemy_Hero.character.potions -= 1
									damage_text = Enemy_Hero.DamageText(Enemy_Hero.character.rect.centerx, Enemy_Hero.character.rect.y, str(heal_amount), asset.green)
									damage_text_group.add(damage_text)
									asset.healup.play()
									asset.current_fighter += 1
									asset.action_cooldown = 0
				else:
					asset.game_over = -1


				#enemy action
				for count, wizard in enumerate(wizard_list2):
					if asset.current_fighter == 2 + count:
						if wizard.alive == True:
							asset.action_cooldown += 1
							if asset.action_cooldown >= asset.action_wait_time:
								#check if wizard needs to heal first
								if (wizard.hp / wizard.max_hp) < 0.5 and wizard.potions > 0:
									#check if the potion would heal the wizard beyond max health
									if wizard.max_hp - wizard.hp > asset.potion_effect:
										heal_amount = asset.potion_effect
									else:
										heal_amount = wizard.max_hp - wizard.hp
									wizard.hp += heal_amount
									wizard.potions -= 1
									damage_text = Enemy_Hero.DamageText(wizard.rect.centerx, wizard.rect.y, str(heal_amount), asset.green)
									damage_text_group.add(damage_text)
									asset.healup.play()
									asset.current_fighter += 1
									asset.action_cooldown = 0
								#attack
								else:
									wizard.attack(Enemy_Hero.character)
			
									asset.current_fighter += 1
									asset.action_cooldown = 0
						else:
							asset.current_fighter += 1

				#if all fighters have had a turn then reset
				if asset.current_fighter > asset.total_fighters_on_3_enemy:
					asset.current_fighter = 1


			#check if all wizard are dead
			alive_wizard = 0
			for wizard in wizard_list2:
				if wizard.alive == True:
					alive_wizard += 1
			if alive_wizard == 0:
				asset.game_over = 1


			#check if game is over
			if asset.game_over != 0:
				if asset.game_over == 1:
					Enemy_Hero.screen.blit(asset.victory_img, (250, 50))
					if restart_button.draw():
						Enemy_Hero.character.reset()
						for wizard in wizard_list2:
							wizard.reset()
						asset.current_fighter = 1
						asset.action_cooldown
						asset.game_over = 0
						level_5 = True
						level_6 = False	
					if level_6_button.draw():
						level_5 = False
						level_6 = True
						Enemy_Hero.character.reset()
						for wizard in wizard_list2:
							wizard.reset()
						asset.current_fighter = 1
						asset.action_cooldown
						asset.game_over = 0		
				if asset.game_over == -1:
					Enemy_Hero.screen.blit(asset.defeat_img, (290, 50))
					if restart_button.draw():
						Enemy_Hero.character.reset()
						for wizard in wizard_list2:
							wizard.reset()
						asset.current_fighter = 1
						asset.action_cooldown
						asset.game_over = 0
						level_1 = True

		elif level_6:
			Enemy_Hero.Display.draw_bg()
			#draw panel
			Enemy_Hero.Display.draw_panel_6()
			if Enemy_Hero.character == nightborne:
				nightborne_health_bar.draw(Enemy_Hero.character.hp)
			else:
				knight_health_bar.draw(Enemy_Hero.character.hp)
			monster1_health_bar.draw(monster1.hp)
			
			#draw fighters
			Enemy_Hero.character.update()
			Enemy_Hero.character.draw()
			for monster in monster_list:
				monster.update()
				monster.draw()

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
			for count, monster in enumerate(monster_list):
				if monster.rect.collidepoint(pos):
					#hide mouse
					pygame.mouse.set_visible(False)
					#show sword in place of mouse cursor
					Enemy_Hero.screen.blit(asset.sword_img, pos)
					if asset.clicked == True and monster.alive == True:
						asset.attack = True
						target = monster_list[count]
			if potion_button.draw():
				asset.potion = True
			#show number of potions remaining
			Enemy_Hero.Display.draw_text(str(Enemy_Hero.character.potions), asset.font, asset.red, 150, Enemy_Hero.screen_height - Enemy_Hero.bottom_panel + 70)


			if asset.game_over == 0:
				#player action
				if Enemy_Hero.character.alive == True:
					if asset.current_fighter == 1:
						asset.action_cooldown += 1
						if asset.action_cooldown >= asset.action_wait_time:
							#look for player action
							#attack
							if asset.attack == True and target != None:
								Enemy_Hero.character.attack(target)
								asset.current_fighter += 1
								asset.action_cooldown = 0
							#potion
							if asset.potion == True:
								if Enemy_Hero.character.potions > 0:
									#check if the potion would heal the player beyond max health
									if Enemy_Hero.character.max_hp - Enemy_Hero.character.hp > asset.potion_effect:
										heal_amount = asset.potion_effect
									else:
										heal_amount = Enemy_Hero.character.max_hp - Enemy_Hero.character.hp
									Enemy_Hero.character.hp += heal_amount
									Enemy_Hero.character.potions -= 1
									damage_text = Enemy_Hero.DamageText(Enemy_Hero.character.rect.centerx, Enemy_Hero.character.rect.y, str(heal_amount), asset.green)
									damage_text_group.add(damage_text)
									asset.healup.play()
									asset.current_fighter += 1
									asset.action_cooldown = 0
				else:
					asset.game_over = -1


				#enemy action
				for count, monster in enumerate(monster_list):
					if asset.current_fighter == 2 + count:
						if monster.alive == True:
							asset.action_cooldown += 1
							if asset.action_cooldown >= asset.action_wait_time:
								#check if monster needs to heal first
								if (monster.hp / monster.max_hp) < 0.5 and monster.potions > 0:
									#check if the potion would heal the monster beyond max health
									if monster.max_hp - monster.hp > asset.potion_effect:
										heal_amount = asset.potion_effect
									else:
										heal_amount = monster.max_hp - monster.hp
									monster.hp += heal_amount
									monster.potions -= 1
									damage_text = Enemy_Hero.DamageText(monster.rect.centerx, monster.rect.y, str(heal_amount), asset.green)
									damage_text_group.add(damage_text)
									asset.healup.play()
									asset.current_fighter += 1
									asset.action_cooldown = 0
								#attack
								else:
									monster.attack(Enemy_Hero.character)
			
									asset.current_fighter += 1
									asset.action_cooldown = 0
						else:
							asset.current_fighter += 1

				#if all fighters have had a turn then reset
				if asset.current_fighter > asset.total_fighters_on_1_enemy:
					asset.current_fighter = 1


			#check if all monster are dead
			alive_monster = 0
			for monster in monster_list:
				if monster.alive == True:
					alive_monster += 1
			if alive_monster == 0:
				asset.game_over = 1


			#check if game is over
			if asset.game_over != 0:
				if asset.game_over == 1:
					Enemy_Hero.screen.blit(asset.victory_img, (250, 50))
					if restart_button.draw():
						Enemy_Hero.character.reset()
						for monster in monster_list:
							monster.reset()
						asset.current_fighter = 1
						asset.action_cooldown
						asset.game_over = 0
						level_6 = True

		
				if asset.game_over == -1:
					Enemy_Hero.screen.blit(asset.defeat_img, (290, 50))
					if restart_button.draw():
						Enemy_Hero.character.reset()
						for monster in monster_list:
							monster.reset()
						asset.current_fighter = 1
						asset.action_cooldown
						asset.game_over = 0
						level_1 = True
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
		if event.type == pygame.MOUSEBUTTONDOWN:
			asset.clicked = True
		else:
			asset.clicked = False

	pygame.display.update()

pygame.quit()