import pygame 

FPS = 60

#tamanho
LARGURA, ALTURA = 960, 720
FILEIRAS, COLUNAS = 8, 8
TAMANHO_CASAS = 720 // COLUNAS

#cores 
PRETO = (0, 0, 0)
BRANCO = (225, 225, 225)
CINZA = (60, 60, 60)
VERMELHO = (220, 0, 0)
VERMELHO_ESCURO = ('#B23535')  
VERMELHO_SOMBRA = ('#792626')  
MARROM = (92,64,51)

#matriz tabuleiro 
matriz = []

# imagens
PECA_BRANCA = pygame.transform.scale(pygame.image.load('assets/peca_branca.png'),(70, 70))
PECA_VERMELHA = pygame.transform.scale(pygame.image.load('assets/peca_vermelha.png'),(70, 70))
COROA = pygame.transform.scale(pygame.image.load('assets/coroa.png'), (45, 25))