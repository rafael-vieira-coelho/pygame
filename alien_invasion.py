#!/usr/bin/env python
# coding: utf8

__AUTHOR__ = "Rafael Vieira Coelho"
__DATE__ = "19/05/2019"

import sys, pygame
import settings as s
from ship import Ship
import game_functions as g
from pygame.sprite import Group
from alien import Alien
from star import Star

def main():
	pygame.init() #inicia o modo gráfico do pygame
	config = s.Settings() #cria o objeto de configurações
	tela = pygame.display.set_mode((config.largura, config.altura)) #janela de 1200 x 800 pixels
	pygame.display.set_caption("Alien Invasion") #define o título
	nave = Ship(config, tela)
	balas = Group()
	aliens = Group()
	stars = Group()
	g.cria_frota(config, tela, aliens)
	g.cria_estrelas(config, tela, stars)
	while True:
		nave.atualiza(config)
		g.atualiza_balas(balas)
		g.atualiza_aliens(config, aliens)
		g.verifica_colisoes(balas, aliens)
		g.testa_eventos(config, tela, nave, balas)
		g.atualiza_tela(config, tela, nave, balas, aliens, stars)
main()
