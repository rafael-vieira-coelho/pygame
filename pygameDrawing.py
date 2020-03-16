#importa os módulos necessários
import pygame
from pygame.locals import *
from pygame.color import THECOLORS as COR

pygame.init()
screenSize = (640, 480)
screen = pygame.display.set_mode(screenSize)
screen.fill((255, 255, 255))
pygame.display.set_caption("Drawing Examples")
clock = pygame.time.Clock()
running = True
print(COR)
while running:
	r = pygame.draw.rect(screen, COR['black'], (12, 20, 50, 100))
	pygame.draw.polygon(screen, COR['blue'], [(100,100), (100,200), (200,100), (200,200)])
	pygame.draw.circle(screen, COR['green'], (150, 300), 50)
	pygame.draw.ellipse(screen, COR['cyan'], r)
	pygame.draw.line(screen, COR['hotpink2'], (300, 350), (500, 300), 10)
	pygame.draw.lines(screen, COR['orangered1'], False, [(600, 400), (500, 300), (100, 400), (100, 200)])
	
	time_passed = clock.tick(30)
	for event in pygame.event.get():
		if event.type == QUIT:
			running = False
		if (event.type == KEYUP and event.key == K_ESCAPE):
			running = False
	pygame.display.update()

pygame.quit()		
