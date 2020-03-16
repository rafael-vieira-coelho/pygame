#importa os módulos necessários
import pygame
from pygame.locals import *

#inicia o pygame
pygame.init()

#define o tamanho e cor da janela
screenSize = (640, 480)
screen = pygame.display.set_mode(screenSize)
screen.fill((255, 255, 255))

# define o título
pygame.display.set_caption("Hello, World!")

#cria o relógio que controla o tempo do jogo
clock = pygame.time.Clock()

running = True
while running:
	#define velocidade
	time_passed = clock.tick(30)
	print(time_passed, "ms") 
	
	#trata eventos
	for event in pygame.event.get():
		if event.type == QUIT:
			running = False
		if (event.type == KEYUP and event.key == K_ESCAPE):
			running = False

	#atualiza o estado do jogo
	
	#redesenha o jogo
	pygame.display.update()

#finaliza o pygame
pygame.quit()		
