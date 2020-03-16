#!/usr/bin/env python
# coding: utf8

__AUTHOR__ = "Rafael Vieira Coelho"
__DATE__ = "19/05/2019"

import pygame
import settings as s
from ship import Ship
import game_functions as g


def main():
    pygame.init()  # inicia o modo gráfico do pygame
    config = s.Settings()  # cria o objeto de configurações
    tela = pygame.display.set_mode((config.largura, config.altura))  # janela de 1200 x 800 pixels
    pygame.display.set_caption("Alien Invasion")  # define o título
    nave = Ship(tela)
    while True:
        g.testa_eventos(nave)
        g.atualiza_tela(config, tela, nave)
        nave.atualiza(config)


main()
