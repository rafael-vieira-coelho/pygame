import pygame
from pygame.locals import *

pygame.init()
screenSize = (640, 480)
screen = pygame.display.set_mode(screenSize)
screen.fill((255, 255, 255))
pygame.display.set_caption("Playing Music")

clock = pygame.time.Clock()

#toca música
pygame.mixer.music.load('music.ogg')
pygame.mixer.music.play(-1)
running = True
while running:
	time_passed = clock.tick(30)
	for event in pygame.event.get():
		if event.type == QUIT:
			running = False
	
	#atualiza o estado do jogo
	
	#redesenha o jogo
	pygame.display.update()

#finaliza o pygame
pygame.quit()		


