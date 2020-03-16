#!/usr/bin/env python
# coding: utf8

__AUTHOR__ = "Rafael Vieira Coelho"
__DATE__ = "19/05/2019"

class Settings():
	
	def __init__(self):
		self.largura = 1200
		self.altura = 800
		self.cor_fundo = (0, 0, 0) #preto
		self.nave_velocidade = 5
		self.nave_altura = 40
		self.bala_velocidade = 15
		self.bala_largura = 3
		self.bala_altura = 15
		self.bala_cor = (255, 255, 255) #branco
		self.balas_maximo = 5
		self.alien_velocidade = 1
		self.frota_velocidade = 5
		self.frota_direcao = 1
