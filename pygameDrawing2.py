import math 
import pygame
from pygame.locals import *
from pygame.color import THECOLORS as COR

pygame.init()
screenSize = (640, 480)
screen = pygame.display.set_mode(screenSize)
screen.fill((0, 0, 0))

clock = pygame.time.Clock()
running = True
while running:
	time_passed = clock.tick(30)
	for event in pygame.event.get():
		if event.type == QUIT:
			running = False

	for i in range(200):
		radians_x = i / 20
		radians_y = i / 6
		x = int(175 * math.sin(radians_x)) + 200
		y = int(175 * math.cos(radians_y)) + 200
 
		pygame.draw.line(screen, COR['green'], [x,y], [x+5,y], 5)
    
	pygame.display.update()
		
pygame.quit()    
