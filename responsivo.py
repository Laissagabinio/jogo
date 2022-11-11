import pygame, sys
from pygame.locals import *

#da pra usar esse script se quiser deixar o jogo em tela cheia 

pygame.init()
pygame.display.set_caption('damas')
tamanho_monitor = [pygame.display.Info().current_w, pygame.display.Info().current_h]
janela = pygame.display.set_mode((500, 500), pygame.RESIZABLE)
VERMELHO_ESCURO = (145,0,0)
 
tela_cheia = False
 
while True:
    janela.fill((0, 0, 50)) #mudar as cores
    #esse retangulo é inutil, pode ser usado como exemplo pra redimensionar outros objetos 
    pygame.draw.rect(janela, (255, 0, 0), pygame.Rect(janela.get_width() - 5 - (janela.get_width() / 5), 50, janela.get_width() / 5, 50))
    #fazer redimensionamento de texto, preguiça
    fonte = pygame.font.Font('freesansbold.ttf', 15)
    texto = fonte.render("quero trancar o curso", True, VERMELHO_ESCURO)
    janela.blit(texto, [30, 150])

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        #faz aquele quadrado q eu nao sei o nome funcionar
        if event.type == VIDEORESIZE:
            if not tela_cheia:
                janela = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
        if event.type == KEYDOWN:
            #usa a tecla ESC pra fechar o jogo
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            #usa a tecla T pra deixar em tela cheia, achei feio mas pode ser util pra outra coisa
            if event.key == K_t:
                tela_cheia = not tela_cheia
                if tela_cheia:
                    janela = pygame.display.set_mode(tamanho_monitor, pygame.FULLSCREEN)
                else:
                    janela = pygame.display.set_mode((janela.get_width(), janela.get_height()), pygame.RESIZABLE)

    pygame.display.update()