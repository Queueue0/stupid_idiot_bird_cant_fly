import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import random

GREEN = (0, 255, 0)
NUMBER_OF_CLOUDS = 6

class Cloud(pygame.sprite.Sprite):
	""" Represents a cloud """
	
	def __init__(self):
		super().__init__()
		num = random.randint(1, NUMBER_OF_CLOUDS)
        
        #my girlfriend made me do this
        #he's whipped -the girlfriend 
		if num == 6:
			self.image = pygame.image.load("resources/thebestcloud.png").convert()
		else:
			self.image = pygame.image.load("resources/cloud_" + str(num) + ".png").convert()
		self.image.set_colorkey(GREEN)
		self.rect = self.image.get_rect()
		
		SCREEN_WIDTH, SCREEN_HEIGHT = pygame.display.get_surface().get_size()
		self.rect.x = SCREEN_WIDTH + 1
		self.rect.y = random.randint(50, SCREEN_HEIGHT - 50 - self.image.get_height())
		
	def update(self):
		self.rect.x -= 3
		if self.rect.right < 0:
			self.kill()
	