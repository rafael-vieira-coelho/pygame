#!/usr/bin/env python
# coding: utf8

__AUTHOR__ = "Rafael Vieira Coelho"
__DATE__ = "21/05/2019"

import pygame
from random import randint 
from pygame.sprite import Sprite

class Star(Sprite):
	
	def __init__(self, config, tela):
		super(Star, self).__init__()
		self.config = config
		self.tela = tela
		#carrega a imagem
		self.nome_imagem = 'imagens/estrela.png'
		self.imagem = pygame.image.load(self.nome_imagem)
		self.retangulo = self.imagem.get_rect()
		self.retangulo.x = randint(0, 1200)
		self.retangulo.y = randint(0, 800)
		self.x = randint(0, 1200)
		self.y = randint(0, 800)

	#desenha a nave na sua posição atual
	def desenha(self):
		self.tela.blit(self.imagem, self.retangulo)

