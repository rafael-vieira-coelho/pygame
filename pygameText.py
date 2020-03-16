#importa os módulos necessários
import pygame
from pygame.locals import *

pygame.init()
screenSize = (640, 480)
screen = pygame.display.set_mode(screenSize)
screen.fill((255, 255, 255))
pygame.display.set_caption("Using Font Example")
clock = pygame.time.Clock()
running = True

# Carrega um arquivo de fonte para o Pygame.
fonte = pygame.font.Font('TheGodfather.ttf', 90)
while running:
	# Cria texto com a fonte carregada
	screen.blit(fonte.render('Ola mundo', True, (255, 0, 0), (0, 0, 255)), (200, 150))

	time_passed = clock.tick(30)
	for event in pygame.event.get():
		if event.type == QUIT:
			running = False
		if (event.type == KEYUP and event.key == K_ESCAPE):
			running = False
	pygame.display.update()

pygame.quit()		
