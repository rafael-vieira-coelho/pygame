#!/usr/bin/env python
# coding: utf8

__AUTHOR__ = "Rafael Vieira Coelho"
__DATE__ = "19/05/2019"

import pygame
from random import randint 
from pygame.sprite import Sprite

class Alien(Sprite):
	
	def __init__(self, config, tela):
		super(Alien, self).__init__()
		self.config = config
		self.velocidade = config.nave_velocidade
		self.tela = tela
		#carrega a imagem
		self.numero_imagem = randint(1,2)
		self.nome_imagem = 'imagens/alien' + str(self.numero_imagem) + '.png'
		self.imagem = pygame.image.load(self.nome_imagem)
		self.retangulo = self.imagem.get_rect()
		self.retangulo.x = self.retangulo.width
		self.retangulo.y = self.retangulo.height
		self.x = float(self.retangulo.x)
		
	#desenha a nave na sua posição atual
	def desenha(self):
		self.tela.blit(self.imagem, self.retangulo)
