import pygame

#cores que vamos usar
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
VERMELHO = (255, 0, 0)
VERMELHO_ESCURO = (145,0,0)    #NÃO SEI SE FICOU UMA COR LEGAL
MARROM = (92,64,51)

#iniciando os módulos do pygame
pygame.init()
janela = pygame.display.set_mode((960,720))
pygame.display.set_caption('Jogo de Damas')

#imagem na página inicial
imagem = pygame.image.load('DAMAS.jpg') 
janela.blit(imagem, (0, 0))


pygame.display.update()

#fazendo a janela ficar aberta e só fechar quando mandarmos
janela_aberta = True

while janela_aberta:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False
pygame.quit()


