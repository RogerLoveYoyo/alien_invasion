# coding=gbk
# game_stats.py by Roger.W on Jan 21th,2019
# ��Ϸͳ����Ϣ

class GameStats():
	"""������Ϸ��ͳ����Ϣ"""
	
	def __init__(self,ai_settings):
		"""��ʼ��ͳ����Ϣ"""
		self.ai_settings = ai_settings
		self.reset_stats()
		
		# ��Ϸ������ʱ���ڷǻ״̬
		self.game_active = False
		
		# ���κ�����¶���Ӧ������ߵ÷�
		self.high_score = 0
		
	def reset_stats(self):
		"""��ʼ������Ϸ�����ڼ�ɱ仯��ͳ����Ϣ"""
		self.ships_left = self.ai_settings.ship_limit
		self.score = 0
		self.level = 1