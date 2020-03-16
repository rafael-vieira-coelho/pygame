#!/usr/bin/env python
# coding: utf8

__AUTHOR__ = "Rafael Vieira Coelho"
__DATE__ = "19/05/2019"

#funções auxiliares
import sys, pygame
from bullet import Bullet
from alien import Alien

#responde a eventos de pressionamento de teclas e mouse
def testa_eventos(config, tela, nave, balas):
	for evento in pygame.event.get(): #verifica todos os eventos ocorridos
		if evento.type == pygame.QUIT: #verifica se a janela foi fechada
			sys.exit()
		elif evento.type == pygame.KEYDOWN: #quando aperta uma tecla
			testa_eventos_aperta_tecla(evento, config, tela, nave, balas)
		elif evento.type == pygame.KEYUP: #quando solta a tecla
			testa_eventos_solta_tecla(evento, nave)
					
#atualiza as imagens na tela e redesenha a mesma
def atualiza_tela(config, tela, nave, balas, aliens):
	tela.fill(config.cor_fundo) #preenche a janela com a cor de fundo		
	nave.desenha() #desenha a nave na tela
	for alien in aliens.sprites():
		alien.desenha()
	for bala in balas.sprites():
		bala.desenha()
	pygame.display.flip() #redesenha a tela			

def testa_eventos_aperta_tecla(evento, config, tela, nave, balas):
	#print(evento.key, chr(evento.key))
	if evento.key == pygame.K_RIGHT: # Move a espaçonave para a direita
		nave.move_direita = True
	elif evento.key == pygame.K_LEFT:# Move a espaçonave para a esquerda
		nave.move_esquerda = True
	elif evento.key == pygame.K_UP: # Move a espaçonave para cima
		nave.move_cima = True
	elif evento.key == pygame.K_DOWN:# Move a espaçonave para baixo
		nave.move_baixo = True
	elif evento.key == pygame.K_SPACE:
		dispara_bala(config, tela, nave, balas)	
	elif evento.key == pygame.K_q: #https://www.pygame.org/docs/ref/key.html
		sys.exit(1)	

def dispara_bala(config, tela, nave, balas):
	if len(balas) < config.balas_maximo:
			nova_bala = Bullet(config, tela, nave)
			balas.add(nova_bala)

def atualiza_balas(balas):
	for bala in balas.sprites():
		if bala.retangulo.bottom <= 0:
			balas.remove(bala)
		else:	
			bala.atualiza()
	print(str(len(balas)) + ' balas')

def cria_frota(config, tela, aliens):
	alien = Alien(config, tela)
	alien_largura = alien.retangulo.width
	alien_altura = alien.retangulo.height
	numero_aliens_y = obtem_numero_linhas_possiveis(config, alien_altura)
	espaco_valido_x = config.largura - alien_largura * 2 #desconta as duas margens
	numero_aliens_x = int(espaco_valido_x / (2 * alien_largura)) + 1 #espaço para a nave e o espaço do lado
	for linha in range(numero_aliens_y):
		for alien_numero in range(numero_aliens_x):
			alien = cria_alien(config, tela, alien_numero, alien_largura, linha)
			aliens.add(alien) 

def cria_alien(config, tela, alien_numero, alien_largura, numero_linha):
	alien = Alien(config, tela)
	alien.x = alien_largura + 2 * alien_largura * alien_numero
	alien.y = alien.retangulo.height + 2 * alien.retangulo.height * numero_linha
	alien.retangulo.x = alien.x
	alien.retangulo.y = alien.y
	return alien

def obtem_numero_linhas_possiveis(config, alien_altura):
	espaco_valido_y = (config.altura - (3 * alien_altura) - config.nave_altura) # 3 vezes pois precisa ter espaço em branco antes, a nave e um espaço em branco depois
	numero_linhas = int(espaco_valido_y / (3 * alien_altura))
	return numero_linhas

def testa_eventos_solta_tecla(evento, nave):
	if evento.key == pygame.K_RIGHT:
		nave.move_direita = False
	elif evento.key == pygame.K_LEFT:
		nave.move_esquerda = False
	elif evento.key == pygame.K_UP:
		nave.move_cima = False
	elif evento.key == pygame.K_DOWN:
		nave.move_baixo = False
