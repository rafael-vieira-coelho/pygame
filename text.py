#!/usr/bin/env python
# coding: utf8

__AUTHOR__ = "Rafael Vieira Coelho"
__DATE__ = "22/05/2019"

import pygame
from random import randint 
from pygame.sprite import Sprite

class Text(Sprite):
	
	def __init__(self, config, tela, msg):
		super(Text, self).__init__()
		self.pontos = int(msg)
		self.config = config
		self.tela = tela
		self.largura, self.altura = 60, 40
		self.cor = (0, 255, 0)
		self.cor_fundo = (0, 0, 0)
		self.fonte = pygame.font.SysFont(None, 48)
		self.retangulo = pygame.Rect(0, 0, self.largura, self.altura)
		self.retangulo.y = config.altura - 30
		self.escreve(msg)
		
	#desenha o alien na sua posição atual
	def escreve(self, msg):
		self.tela.fill(self.cor_fundo, self.retangulo)
		self.mensagem_renderizada = self.fonte.render(msg, True, self.cor, self.cor_fundo)

	#atualiza a posicao do alien
	def desenha(self):
		self.tela.fill(self.cor_fundo, self.retangulo)
		self.tela.blit(self.mensagem_renderizada, self.retangulo)
			

