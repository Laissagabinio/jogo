import pygame
from .constantes import VERMELHO, PRETO, BRANCO, FILEIRAS, COLUNAS, TAMANHO_CASAS

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
        matriz = []

        for i in range(8): #8 são as quantidades de fileiras
            #P é se a casa for preta e B é se a casa for branca
            if i % 2 == 0:
                matriz.append(['p','b','p','b','p','b','p','b'])
            else:
                matriz.append(['b','p','b','p','b','p','b', 'p'])

        y = 0
        for largura in range(len(matriz)):
            x = 0
            for altura in range(len(matriz[largura])):
                #ele vai passar lendo cada altura e cada largura, se coincidir com o P, ele vai deixar preto e também fazer a peça vermelha
                if matriz[largura][altura] == 'p':
                    pygame.draw.rect(janela, PRETO, (x, y, TAMANHO_CASAS, TAMANHO_CASAS))
                    pygame.draw.circle(janela, VERMELHO, (x + 45,y + 45), 15, 0)
                else:
                    pygame.draw.rect(janela, BRANCO, (x, y, TAMANHO_CASAS, TAMANHO_CASAS))
                x += TAMANHO_CASAS
            y += TAMANHO_CASAS     
