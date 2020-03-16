#!/usr/bin/env python
# coding: utf8

__AUTHOR__ = "Rafael Vieira Coelho"
__DATE__ = "19/05/2019"

import pygame

from random import randint 

class Ship():
	
	def __init__(self, tela):
		self.velocidade = 5
		self.tela = tela
		#carrega a imagem
		self.numero_imagem = randint(1,6)
		self.nome_imagem = 'imagens/nave' + str(self.numero_imagem) + '.png'
		self.imagem = pygame.image.load(self.nome_imagem)
		self.retangulo = self.imagem.get_rect()
		self.retangulo_tela = tela.get_rect()
		#coloca a imagem na parte inferior da tela
		self.retangulo.centerx = self.retangulo_tela.centerx
		self.retangulo.bottom = self.retangulo_tela.bottom
		self.move_direita = False
		self.move_esquerda = False
		self.move_cima = False
		self.move_baixo = False
		
	#desenha a nave na sua posição atual
	def desenha(self):
		self.tela.blit(self.imagem, self.retangulo)

	#atualiza a posição da espaçonave de acordo com a flag de movimento
	def atualiza(self, config):
		if self.move_direita and self.retangulo.right < config.largura:
			self.retangulo.centerx += self.velocidade
		elif self.move_esquerda and self.retangulo.left > 0:
			self.retangulo.centerx -= self.velocidade	
		elif self.move_baixo:
			self.retangulo.centery += self.velocidade
		elif self.move_cima:
			self.retangulo.centery -= self.velocidade			
