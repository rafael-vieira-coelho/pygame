#!/usr/bin/env python
# coding: utf8

__AUTHOR__ = "Rafael Vieira Coelho"
__DATE__ = "20/05/2019"

import pygame
from pygame.sprite import Sprite

class Bullet(Sprite): #https://github.com/myint/pygame/blob/master/lib/sprite.py
	
	def __init__(self, config, tela, nave):
		super(Bullet, self).__init__()
		self.tela = tela
		self.retangulo = pygame.Rect(0, 0, config.bala_largura, config.bala_altura)
		self.retangulo.centerx = nave.retangulo.centerx
		self.retangulo.top = nave.retangulo.top
		self.y = float(self.retangulo.y)
		self.cor = config.bala_cor
		self.velocidade = config.bala_velocidade
		
	def atualiza(self):
		self.y -= self.velocidade
		self.retangulo.y = self.y	
		
	def desenha(self):
		pygame.draw.rect(self.tela, self.cor, self.retangulo)	
