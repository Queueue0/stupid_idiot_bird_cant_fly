import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import random
import math

WHITE = (255,255,255)
PIPE_HEIGHT = 860.0
PIPE_WIDTH = 75.0

class Top_pipe(pygame.sprite.Sprite):
	"""
	Represents the top pipe
	Derived from Sprite class in pygame
	"""

	def __init__(self, bottom_pipe, scorezone_height = 200):
		super().__init__()
		
		SCREEN_WIDTH, SCREEN_HEIGHT = pygame.display.get_surface().get_size()
		self.h_scale = SCREEN_WIDTH / 1280
		self.v_scale = SCREEN_HEIGHT / 720

		self.image = pygame.image.load("resources/top_pipe.png").convert()
		self.image = pygame.transform.scale(self.image, (int(PIPE_WIDTH * self.h_scale), int(PIPE_HEIGHT * self.v_scale)))
		self.image.set_colorkey(WHITE)
		self.rect = self.image.get_rect()
		self.rect.x = bottom_pipe.rect.x
		self.rect.y = bottom_pipe.rect.y - ((PIPE_HEIGHT + scorezone_height) * self.v_scale)

	def update(self):
		self.rect.x -= int(5 * self.h_scale)
		if self.rect.right <= 0:
			self.kill()

class Bottom_pipe(pygame.sprite.Sprite):
	"""
	Represents the bottom pipe
	Derived from Sprite class in pygame
	"""

	def __init__(self, scorezone_height = 200):
		super().__init__()
		
		SCREEN_WIDTH, SCREEN_HEIGHT = pygame.display.get_surface().get_size()
		self.h_scale = SCREEN_WIDTH / 1280
		self.v_scale = SCREEN_HEIGHT / 720

		self.image = pygame.image.load("resources/bottom_pipe.png").convert()
		self.image = pygame.transform.scale(self.image, (int(PIPE_WIDTH * self.h_scale), int(PIPE_HEIGHT * self.v_scale)))
		self.image.set_colorkey(WHITE)
		self.rect = self.image.get_rect()
		
		MAGIC_HEIGHT_NUM = math.ceil((SCREEN_HEIGHT - (600 * self.v_scale)) / 2)
		self.rect.x = SCREEN_WIDTH + 1
		self.rect.y = random.randint(math.ceil(scorezone_height * self.v_scale + MAGIC_HEIGHT_NUM), math.ceil(SCREEN_HEIGHT - MAGIC_HEIGHT_NUM))

	def update(self):
		self.rect.x -= int(5 * self.h_scale)
		if self.rect.right <= 0:
			self.kill()

class Between_pipe(pygame.sprite.DirtySprite):

	def __init__(self, bottom_pipe, scorezone_height = 200):
		super().__init__()

		SCREEN_WIDTH, SCREEN_HEIGHT = pygame.display.get_surface().get_size()
		self.h_scale = SCREEN_WIDTH / 1280
		self.v_scale = SCREEN_HEIGHT / 720
		
		self.image = pygame.Surface([PIPE_WIDTH * self.h_scale, scorezone_height * self.v_scale])
		self.rect = self.image.get_rect()
		self.rect.x = bottom_pipe.rect.x
		self.rect.y = bottom_pipe.rect.y - int(scorezone_height * self.v_scale)
		self.visible = 0

	def update(self):
		self.rect.x -= int(5 * self.h_scale)
		if self.rect.right <= 0:
			self.kill()
