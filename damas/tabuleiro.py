import pygame
from .constantes import PRETO, BRANCO, FILEIRAS, COLUNAS, TAMANHO_CASAS

class Tabuleiro:
    def __init__(self):
        #depois eu coloco as peças dentro dessa lista 
        self.tabuleiro = []
        self.peça_selecionada = None
        #essa é a quantidade de peças q tem no começo do jogo
        self.branco_peças = self.vermelho_peças = 12
        #quantidade de damas no começo
        self.branco_damas = self.vermelho_damas = 0

    def desenhar_quadrados(self, janela):
        janela.fill(PRETO) 
        for fileira in range(FILEIRAS):
            #esse fileira%2 serve pra fazer dois tipos de padrões,
            #um começando com branco, q vale 0 e outro preto valendo 1, quando usa %2 desenha a cada duas casas
            for coluna in range(fileira % 2, FILEIRAS, 2):
                pygame.draw.rect(janela, BRANCO, (fileira * TAMANHO_CASAS, coluna * TAMANHO_CASAS, TAMANHO_CASAS, TAMANHO_CASAS))
