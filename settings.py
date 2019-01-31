# coding=gbk
# settings.py by Roger.W on Jan 11th,2019
# ������
class Settings():
	"""�洢�����������֡��������õ���"""
	
	def __init__(self):
		"""��ʼ����Ϸ��̬����"""
		self.screen_width = 800
		self.screen_height = 600
		self.bg_color = (0,0,0)
	
		#�ɴ�������
		# self.ship_speed_factor = 1.5
		self.ship_limit = 2
		
		# �ӵ�����
		# self.bullet_speed_factor = 3
		self.bullet_width = 3
		self.bullet_height = 3
		self.bullet_color = (255,255,255)
		self.bullets_allowed = 5
		
		# ����������
		# self.alien_speed_factor = 0.5
		self.fleet_drop_speed = 10
		# fleet_directionΪ1��ʾ���ƣ�Ϊ-1��ʾ����
		#self.fleet_direction = 1
		
		# ��ʲô�����ٶȼӿ���Ϸ����
		self.speedup_scale = 1.1
		# �����˵�������ٶ�
		self.score_scale = 1.5
		
		self.initialize_dynamic_settings()
		
	def initialize_dynamic_settings(self):
		"""��ʼ������Ϸ���ж��仯������"""
		self.ship_speed_factor = 1.5
		self.bullet_speed_factor = 3
		self.alien_speed_factor = 0.5
		
		# �Ƿ�
		self.alien_points = 10
		# fleet_directionΪ1��ʾ���ƣ�Ϊ-1��ʾ����
		self.fleet_direction = 1
		
	def increase_speed(self):
		"""����ٶ����ú������˵���"""
		self.ship_speed_factor *= self.speedup_scale
		self.bullet_speed_factor *= self.speedup_scale
		self.alien_speed_factor *= self.speedup_scale
		
		self.alien_points = int(self.alien_points * self.score_scale)
		#print(self.alien_points)
		