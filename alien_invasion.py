# coding=gbk
# alien_invasion.py by Roger.W on Jan 11th,2019
# 外星人游戏主程序？
import sys

import pygame
from pygame.sprite import Group

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
from alien import Alien
import game_functions as gf

def run_game():
	# 初始化游戏并创建一个屏幕对象
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode(
		(ai_settings.screen_width,ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")
	
	# 创建Play按钮
	play_button = Button(ai_settings,screen,"Play")
	
	# 创建存储游戏统计信息的实例，并创建记分牌
	stats = GameStats(ai_settings)
	sb = Scoreboard(ai_settings,screen,stats)
	
	# 创建一艘飞船、一个子弹编组和一个外星人编组
	ship = Ship(ai_settings,screen)
	bullets = Group()
	aliens = Group()
	
	# 创建外星人群
	gf.create_fleet(ai_settings,screen,ship,aliens)
	
	# 开始游戏的主循环
	while True:
		
		# 监视键盘和鼠标事件
		gf.check_events(ai_settings,screen,stats,sb,play_button,ship,
			aliens,bullets)
		
		if stats.game_active:
			ship.update()
			gf.update_bullets(ai_settings,screen,stats,sb,ship,aliens,
				 bullets)
			gf.update_aliens(ai_settings,screen,stats,sb,ship,aliens,bullets)
					
		# 每次循环时都重绘屏幕			
		# 让最近绘制的屏幕可见
		gf.update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,
			play_button)
		
run_game()
