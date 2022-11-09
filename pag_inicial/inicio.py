import pygame

#cores que vamos usar
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
VERMELHO = (255, 0, 0)
VERMELHO_ESCURO = (145,0,0)    #NÃO SEI SE FICOU UMA COR LEGAL

#iniciando os módulos do pygame
pygame.init()
janela = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Jogo de Damas')

#página inicial (desenhos)
janela.fill(PRETO)  #fundo preto
fonte = pygame.font.Font('freesansbold.ttf', 48)  #NÃO SEI SE FICOU UMA FONTE LEGAL
texto = fonte.render("DAMAS", True, VERMELHO_ESCURO)
janela.blit(texto, [30, 150])


pygame.display.update()

#fazendo a janela ficar aberta e só fechar quando mandarmos
janela_aberta = True

while janela_aberta:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False
pygame.quit()


