import pygame
from .constantes import PRETO, BRANCO, VERMELHO, FILEIRAS, COLUNAS, TAMANHO_CASAS, COROA, PECA_BRANCA, PECA_VERMELHA


class Peca:
    def __init__(self, fileira, coluna, cor):
        self.fileira = fileira
        self.coluna = coluna
        self.cor = cor 
        self.dama = False
        self.x = 0
        self.y = 0
        self.posição()
        
    # chamar essa função quando a peça chegar no final do tabuleiro
    def torna_dama(self):
        self.dama = True

    def desenhar(self, janela):
        # tem outra função igual no tabuleiro, quando eu chamo ela no inicio ele desenha o tabuleiro e as peças ao mesmo tempo
        #pygame.draw.circle(janela, self.cor, (self.x, self.y), 30, 0)
        if self.cor == BRANCO:
            janela.blit(PECA_BRANCA,(self.x - PECA_BRANCA.get_width()//2, self.y - PECA_BRANCA.get_height()//2)) 
        elif self.cor == VERMELHO:
            janela.blit(PECA_VERMELHA,(self.x - PECA_VERMELHA.get_width()//2, self.y - PECA_VERMELHA.get_height()//2))
        if self.dama:
            janela.blit(COROA, (self.x - COROA.get_width()//2, self.y - COROA.get_height()//2))

    def posição(self):
        self.y = TAMANHO_CASAS * self.fileira + TAMANHO_CASAS // 2
        self.x = TAMANHO_CASAS * self.coluna + TAMANHO_CASAS // 2

    def mover(self, fileira, coluna):
        self.fileira = fileira 
        self.coluna = coluna
        self.posição()



    





