# coding=gbk
# ship.py by Roger.W on Jan 14th,2019
# �ɴ�
import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
	
	def __init__(self,ai_settings,screen):
		"""��ʼ���ɴ����������ʼλ��"""
		super(Ship,self).__init__()
		self.screen = screen
		self.ai_settings = ai_settings
		
		# ���طɴ�ͼ�񲢻�ȡ����Ӿ���
		self.image  = pygame.image.load('images/ship.png')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		
		# ��ÿ���·ɴ�������Ļ�ײ�����
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom
		
		# �ڷɴ�����center�д洢С��ֵ
		self.center = float(self.rect.centerx)
		self.bottom = float(self.rect.bottom)
		
		# �ƶ���־
		self.moving_right = False
		self.moving_left = False
		#self.moving_up = False
		#self.moving_down = False
		
	def update(self):
		"""�����ƶ���־�����ɴ���λ��"""
		# ���·ɴ���centerֵ��������rect
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.center += self.ai_settings.ship_speed_factor
		if self.moving_left and self.rect.left > 0:
			self.center -= self.ai_settings.ship_speed_factor
		# �����ƶ�	
		#if self.moving_up and self.rect.top > self.screen_rect.top:
		#	self.bottom -= self.ai_settings.ship_speed_factor
		#if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
		#	self.bottom += self.ai_settings.ship_speed_factor
			
		# ����self.senter����rect����
		self.rect.centerx = self.center
		#self.rect.bottom = self.bottom
			
	def blitme(self):
		"""��ָ��λ�û��Ʒɴ�"""
		self.screen.blit(self.image,self.rect)
		
	def center_ship(self):
		"""�÷ɴ�����Ļ�Ͼ���"""
		self.center = self.screen_rect.centerx
		

