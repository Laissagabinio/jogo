import pygame
from .constantes import BRANCO, VERMELHO, FILEIRAS, TAMANHO_CASAS



class Peca:
    def __init__(self):
        '''self.x = 0
        self.y = 0'''
    
    '''def add_janela(self, janela):
        self.janela = janela
'''
    def add_x (self, x):
        self.x = x

    def add_y (self,y):
        self.y = y
        
    def desenha_peca(self, janela):
       ''' peça_vermelha = pygame.draw.circle(janela, VERMELHO, (self.x,self.y), 15, 0)
        peça_branca = pygame.draw.circle(janela, BRANCO, (self.x,self.y), 15, 0)'''
''' for fileira in range(FILEIRAS):
            #esse fileira%2 serve pra fazer dois tipos de padrões,
            #um começando com branco, q vale 0 e outro preto valendo 1, quando usa %2 desenha a cada duas casas
            for coluna in range(fileira % 2, FILEIRAS, 2):
                if fileira%2 == 1:
                    pygame.draw.circle(janela, VERMELHO, (fileira * TAMANHO_CASAS-(TAMANHO_CASAS /2), coluna * (TAMANHO_CASAS) /2),10)
                else:
                    break'''
                



