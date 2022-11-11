import pygame

#tamanho
LARGURA = 960
ALTURA = 720

#cores que vamos usar
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
VERMELHO = (255, 0, 0)
VERMELHO_ESCURO = ('#B23535')  
VERMELHO_SOMBRA = ('#792626')  
MARROM = (92,64,51)

#iniciando os módulos do pygame
pygame.init()
pygame.display.set_caption('Jogo de Damas')

janela = pygame.display.set_mode((960,720))
janela_aberta = True

pygame.draw.rect(janela, VERMELHO_ESCURO, pygame.Rect(30, 30, 60, 60),  2, 3)


#padrão dos textos
def textos(texto, font, color):
	textSurface = font.render(texto, True, color)
	return textSurface, textSurface.get_rect()

#CRIAR BOTÃO
def criar_botao(texto, retangulo, VERMELHO_ESCURO, VERMELHOR_SOMBRA, BRANCO, acao=None):
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

	fontePequena = pygame.font.SysFont('comicsansms', 20)
	surface_texto, rect_texto = textos(texto, fontePequena, BRANCO)
	rect_texto.center = (retangulo[0] + 60, retangulo[1] + 20)
	janela.blit(surface_texto, rect_texto)


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
		criar_botao("VOLTAR",(LARGURA - 200, ALTURA / 2, 120, 40), VERMELHO_ESCURO, VERMELHO_SOMBRA, BRANCO, menu)
	
		

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
		criar_botao("VOLTAR",(LARGURA - 200, ALTURA / 2, 120, 40), VERMELHO_ESCURO, VERMELHO_SOMBRA, BRANCO, menu)
	
		

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
		pygame.display.update()



    
menu()



