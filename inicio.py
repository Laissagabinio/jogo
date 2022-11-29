import pygame, sys, os
from pygame.locals import*

from damas.constantes import LARGURA, ALTURA, FPS, TAMANHO_CASAS, PRETO, BRANCO, VERMELHO, VERMELHO_ESCURO, VERMELHO_SOMBRA, MARROM, CINZA
from damas.tabuleiro import Tabuleiro
from jogo import Jogo

#iniciando os módulos do pygame
pygame.init()
pygame.display.set_caption('Jogo de Damas')

janela = pygame.display.set_mode((960,720))
janela_aberta = True

pygame.draw.rect(janela, VERMELHO_ESCURO, pygame.Rect(30, 30, 60, 60),  2, 3)


#leva pra tela do jogo
def main():
    janela_aberta = True
    #esse relogio é pra deixar com o mesmo FPS em qualquer pc
    clock = pygame.time.Clock()
    jogo = Jogo(janela)

    while janela_aberta:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                janela_aberta = False
				
            if event.type == pygame.MOUSEBUTTONDOWN:
				#preguiça de fazer essa parte 
                posição = pygame.mouse.get_pos()
                fileira, coluna = posição_mouse(posição)
                jogo.selecionar(fileira, coluna)

        '''tabuleiro.desenhar(janela)
        pygame.display.update()'''
        jogo.update()
       
    pygame.quit()

def posição_mouse(posição):
	x, y = posição 
	coluna = x // TAMANHO_CASAS
	fileira = y // TAMANHO_CASAS	
	return fileira, coluna

#padrão dos textos
def textos(texto, font, color):
	textSurface = font.render(texto, True, color)
	return textSurface, textSurface.get_rect()

#CRIAR BOTÃO
def criar_botao(texto, retangulo, VERMELHO_ESCURO, VERMELHO_SOMBRA, BRANCO, acao=None):
	mouse = pygame.mouse.get_pos()
	clique = pygame.mouse.get_pressed()
	raio_borda = 10

	if retangulo[0] + retangulo[2] > mouse[0] > retangulo[0] and retangulo[1] + retangulo[3] > mouse[1] > retangulo[1]:
		pygame.draw.rect(janela, VERMELHO_ESCURO, pygame.Rect(retangulo), 20, raio_borda)
		if clique[0] == 1 and acao != None:
			acao()
	else:
		#nem eu sei como fiz funcionar 
		pygame.draw.rect(janela, VERMELHO_SOMBRA, pygame.Rect(retangulo), 20, raio_borda)

	tamanho_texto = 18
	fonte = pygame.font.Font('assets/Copperplate_Gothic_Light.ttf', tamanho_texto)
	janela_texto, rect_texto = textos(texto, fonte, BRANCO)
	rect_texto.center = (retangulo[0] + 60, retangulo[1] + 20)
	janela.blit(janela_texto, rect_texto)



# SAIR DO JOGO
def sair():
	pygame.quit()
	quit()

#CŔEDITOS 
def creditos():

	imagem = pygame.image.load('assets/fundoC.png') #essa imagem de fundo é a que tem a coroa em cima do nome "devs"
	janela.blit(imagem, (0, 0))
	janela_aberta = True
	
	while janela_aberta:
		for event in pygame.event.get():

			#para fechar a página
			if event.type == pygame.QUIT:
				pygame.quit()
				exit()

		#botão para voltar para o menu	
		criar_botao("VOLTAR",(LARGURA - 200, ALTURA - 100, 120, 40), VERMELHO_ESCURO, VERMELHO_SOMBRA, BRANCO, menu)
	
		#textos 
		tamanho_texto = 28
		fonte = pygame.font.Font('assets/Copperplate_Gothic_Light.ttf', tamanho_texto)

		pygame.draw.rect(janela, VERMELHO_SOMBRA, (350,160,260,190))
		#não consegui colocar aqui a borda arredondada, esqueci completamente como faz
		pygame.draw.line(janela,PRETO,(435,205),(520,205),3)
		#linha que fica embaixo do nome "Devs"
		janela_texto, rect_texto = textos('Devs:', fonte, PRETO)
		rect_texto.center = ((LARGURA /2), ALTURA / 3.7)
		janela.blit(janela_texto, rect_texto)

		janela_texto, rect_texto = textos('Laíssa Gabinio', fonte, PRETO)
		rect_texto.center = ((LARGURA /2), ALTURA / 3)
		janela.blit(janela_texto, rect_texto)

		janela_texto, rect_texto = textos('Yara Barreto', fonte, PRETO)
		rect_texto.center = ((LARGURA /2), ALTURA / 2.5)
		janela.blit(janela_texto, rect_texto)

		pygame.draw.rect(janela, VERMELHO_SOMBRA, (300,400,370,45))
		janela_texto, rect_texto = textos('Versão Python: 3.10.6', fonte, PRETO)
		rect_texto.center = ((LARGURA /2), ALTURA / 1.7)
		janela.blit(janela_texto, rect_texto)
		
		pygame.draw.rect(janela, VERMELHO_SOMBRA, (300,475,370,45))
		janela_texto, rect_texto = textos('Versão Pygame: 2.1.2', fonte, PRETO)
		rect_texto.center = ((LARGURA /2), ALTURA / 1.45)
		janela.blit(janela_texto, rect_texto)

		pygame.display.update()
	

#REGRAS DO JOGO
def regras():
	imagem = pygame.image.load('assets/REGRAS.png') 
	janela.blit(imagem, (0, 0))
	janela_aberta = True
	
	while janela_aberta:
		for event in pygame.event.get():

			#para fechar a página
			if event.type == pygame.QUIT:
				pygame.quit()
				exit()

		#botão para voltar para o menu	
		criar_botao("VOLTAR",(LARGURA - 200, ALTURA - 100, 120, 40), VERMELHO_ESCURO, VERMELHO_SOMBRA, BRANCO, menu)
	
		#textos 
		tamanho_texto = 22
		x_alinhamento = 65
		y_alinhamaneto = 55

		fonte = pygame.font.Font('assets/Copperplate_Gothic_Light.ttf', tamanho_texto)

		#tem muita regra aaaaa
		regra1 = fonte.render('> O jogo é praticado em um tabuleiro de 64 casas, claras e escuras.', True, (PRETO))
		regra2 = fonte.render('> O objetivo é imobilizar ou capturar todas as peças do adversário.', True, (PRETO))
		regra3 = fonte.render('> A peça movimenta-se em diagonal, para frente e uma casa de cada vez.', True, (PRETO))
		regra4 = fonte.render('> A peça é promovida à dama quando atinge o final do tabuleiro.', True, (PRETO))
		regra5 = fonte.render('> A dama pode andar quantas casa quiser para frente e para trás.', True, (PRETO))
		regra6 = fonte.render('> A dama não pode saltar uma peça da mesma cor.', True, (PRETO))
		regra7 = fonte.render('> Quando possível, a captura é obrigatória.', True, (PRETO))
		regra8 = fonte.render('> Deve ser executado o movimento que captura mais peças.', True, (PRETO))
		regra9 = fonte.render('> Não é permitido sopro.', True, (PRETO))
		regra10 = fonte.render('> Duas ou mais peças consecutivas na mesma diagonal', True, (PRETO))
		regra11 = fonte.render('não podem ser capturadas.', True, (PRETO))
		#só pra deixar pronto, depois eu formato tudo bonitinho

		#posição dos textos, me lembre de fazer alguma variavel pra nao precisar usar esse monte de numero feio
		janela.blit(regra1, (x_alinhamento, y_alinhamaneto))
		janela.blit(regra2, (x_alinhamento, y_alinhamaneto*2))
		janela.blit(regra3, (x_alinhamento, y_alinhamaneto*3))
		janela.blit(regra4, (x_alinhamento, y_alinhamaneto*4))
		janela.blit(regra5, (x_alinhamento, y_alinhamaneto*5))
		janela.blit(regra6, (x_alinhamento, y_alinhamaneto*6))
		janela.blit(regra7, (x_alinhamento, y_alinhamaneto*7))
		janela.blit(regra8, (x_alinhamento, y_alinhamaneto*8))
		janela.blit(regra9, (x_alinhamento, y_alinhamaneto*9))
		janela.blit(regra10, (x_alinhamento, y_alinhamaneto*10))
		janela.blit(regra11, (x_alinhamento+19, y_alinhamaneto*11-10))

		pygame.display.update()


#TELA DE MENU
def menu():
	imagem = pygame.image.load('assets/sembotao.png') 
	janela.blit(imagem, (0, 0))
	janela_aberta = True

	while janela_aberta:
		for event in pygame.event.get():
			#para fechar a página
			if event.type == pygame.QUIT:
				pygame.quit()
				exit()
		
		criar_botao("JOGAR",(LARGURA - 760, ALTURA / 2, 120, 40), VERMELHO_ESCURO, VERMELHO_SOMBRA, BRANCO, main)
		criar_botao("REGRAS",(LARGURA - 560, ALTURA / 2, 120, 40), VERMELHO_ESCURO, VERMELHO_SOMBRA, BRANCO, regras)
		criar_botao("CREDITOS",(LARGURA - 360, ALTURA / 2, 120, 40), VERMELHO_ESCURO, VERMELHO_SOMBRA, BRANCO, creditos)
		criar_botao("SAIR",(LARGURA - 560, ALTURA - 250, 120, 40), VERMELHO_ESCURO, VERMELHO_SOMBRA, BRANCO, sair)

		pygame.display.update()



menu()



