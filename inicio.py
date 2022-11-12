import pygame

from damas.constantes import LARGURA, ALTURA, FPS
from damas.constantes import PRETO, BRANCO, VERMELHO, VERMELHO_ESCURO, VERMELHO_SOMBRA, MARROM
from damas.tabuleiro import Tabuleiro


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
	#transforma o script tabuleiro.py em um objeto
    tabuleiro = Tabuleiro()

    while janela_aberta:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                janela_aberta = False
            if event.type == pygame.MOUSEBUTTONDOWN:
				#preguiça de fazer essa parte 
                pass

        tabuleiro.desenhar_quadrados(janela)
        pygame.display.update()

    pygame.quit()


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

	fonte = pygame.font.SysFont('comicsansms', 20)
	janela_texto, rect_texto = textos(texto, fonte, BRANCO)
	rect_texto.center = (retangulo[0] + 60, retangulo[1] + 20)
	janela.blit(janela_texto, rect_texto)



# SAIR DO JOGO
def sair():
	pygame.quit()
	quit()

#CŔEDITOS 
def creditos():

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
		tamanho_texto = 30
		fonte = pygame.font.SysFont('timesnewroman', tamanho_texto)

		janela_texto, rect_texto = textos('aaaaaaaaaaaa', fonte, PRETO)
		rect_texto.center = ((LARGURA /2), ALTURA / 3)
		janela.blit(janela_texto, rect_texto)

		janela_texto, rect_texto = textos('aaaaaaaaaaaaaaaaaa', fonte, PRETO)
		rect_texto.center = ((LARGURA /2), ALTURA / 2.5)
		janela.blit(janela_texto, rect_texto)

		janela_texto, rect_texto = textos('Versão Python: 3.10.6', fonte, PRETO)
		rect_texto.center = ((LARGURA /2), ALTURA / 1.7)
		janela.blit(janela_texto, rect_texto)

		janela_texto, rect_texto = textos('Versão Pygame: 2.1.2', fonte, PRETO)
		rect_texto.center = ((LARGURA /2), ALTURA / 1.5)
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
		tamanho_texto = 30
		x_alinhamento = 50

		fonte = pygame.font.SysFont('timesnewroman', tamanho_texto)
		
		#tem muita regra aaaaa
		regra1 = fonte.render('O jogo é praticado em um tabuleiro de 64 casas, claras e escuras.', 10, (PRETO))
		regra2 = fonte.render('O objetivo é imobilizar ou capturar todas as peças do adversário.', 10, (PRETO))
		regra3 = fonte.render('A peça movimenta-se em diagonal, para frente e uma casa de cada vez.', 10, (PRETO))
		regra4 = fonte.render('Quando a peça atinge a oitava linha do tabuleiro ela é promovida à dama.', 10, (PRETO))
		regra5 = fonte.render('A dama pode andar quantas casa quiser para frente e para trás.', 10, (PRETO))
		regra6 = fonte.render('A dama não pode saltar uma peça da mesma cor.', 10, (PRETO))
		regra7 = fonte.render('Quando possível, a captura é obrigatória.', 10, (PRETO))
		regra8 = fonte.render('Em casos com mais de um modo de captura, deve ser executado o que captura mais peças.', 10, (PRETO))
		regra9 = fonte.render('Não é permitido sopro.', 10, (PRETO))
		regra10 = fonte.render('Duas ou mais peças juntas na mesma diagonal não podem ser capturadas.', 10, (PRETO))
		#só pra deixar pronto, depois eu formato tudo bonitinho

		#posição dos textos, me lembre de fazer alguma variavel pra nao precisar usar esse monte de numero feio
		janela.blit(regra1, (x_alinhamento, 60))
		janela.blit(regra2, (x_alinhamento, 100))
		janela.blit(regra3, (x_alinhamento, 140))
		janela.blit(regra4, (x_alinhamento, 180))
		janela.blit(regra5, (x_alinhamento, 220))
		janela.blit(regra6, (x_alinhamento, 260))
		janela.blit(regra7, (x_alinhamento, 300))
		janela.blit(regra8, (x_alinhamento, 340))
		janela.blit(regra9, (x_alinhamento, 380))
		janela.blit(regra10, (x_alinhamento, 420))

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
		
		criar_botao("SAIR",(LARGURA - 760, ALTURA / 2, 120, 40), VERMELHO_ESCURO, VERMELHO_SOMBRA, BRANCO, sair)
		criar_botao("REGRAS",(LARGURA - 560, ALTURA / 2, 120, 40), VERMELHO_ESCURO, VERMELHO_SOMBRA, BRANCO, regras)
		criar_botao("CREDITOS",(LARGURA - 360, ALTURA / 2, 120, 40), VERMELHO_ESCURO, VERMELHO_SOMBRA, BRANCO, creditos)
		criar_botao("JOGAR",(LARGURA - 560, ALTURA - 250, 120, 40), VERMELHO_ESCURO, VERMELHO_SOMBRA, BRANCO, main)

		pygame.display.update()



menu()



