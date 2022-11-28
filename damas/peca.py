import pygame
from .constantes import PRETO, BRANCO, VERMELHO, FILEIRAS, COLUNAS, TAMANHO_CASAS, COROA


class Peca:
    def __init__(self, coluna, fileira, cor):
        self.coluna = coluna
        self.fileira = fileira
        self.cor = cor 
        self.dama = False
        self.x = 0
        self.y = 0
        self.posição()
    
    # chamar essa função quando a peça chegar no final do tabuleiro
    def torna_dama(self):
        self.dama = True
        
    def posição(self):
        self.x = TAMANHO_CASAS * self.fileira + TAMANHO_CASAS // 2
        self.y = TAMANHO_CASAS * self.coluna + TAMANHO_CASAS // 2

    def desenhar(self, janela):
        # tem outra função igual no tabuleiro, quando eu chamo ela no inicio ele desenha o tabuleiro e as peças ao mesmo tempo
        pygame.draw.circle(janela, self.cor, (self.x, self.y), 30, 0)
        if self.dama:
            janela.blit(COROA, (self.x - 50, self.y + 50))

    def mover(self, fileira, coluna):
        self.fileira = fileira 
        self.coluna = coluna
        self.posição()


    





