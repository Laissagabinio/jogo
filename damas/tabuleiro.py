import pygame
from .constantes import VERMELHO, PRETO, BRANCO, CINZA, FILEIRAS, COLUNAS, TAMANHO_CASAS
from .pecas import Peca

class Tabuleiro:
    def __init__(self):
        #depois eu coloco as peças dentro dessa lista 
        self.tabuleiro = []
        self.peça_selecionada = None
        #essa é a quantidade de peças q tem no começo do jogo
        self.branco_peças = self.vermelho_peças = 12
        #quantidade de damas no começo
        self.branco_damas = self.vermelho_damas = 0
        self.criar_tabuleiro()

    def desenhar_quadrados(self, janela):
        janela.fill(PRETO) 
        pygame.draw.rect(janela, CINZA, pygame.Rect(720, 0, 240, 960)) 
         
        for fileira in range(FILEIRAS):
            #esse fileira%2 serve pra fazer dois tipos de padrões,
            #um começando com branco, q vale 0 e outro preto valendo 1, quando usa %2 desenha a cada duas casas
            for coluna in range(fileira % 2, FILEIRAS, 2):
                pygame.draw.rect(janela, BRANCO, (fileira * TAMANHO_CASAS, coluna * TAMANHO_CASAS, TAMANHO_CASAS, TAMANHO_CASAS))
        #pygame.display.update()

    def criar_tabuleiro(self):
        # eu tentei fazer com matriz mas fiquei muito confusa :(

        for fileira in range(FILEIRAS):
            self.tabuleiro.append([])
            for coluna in range(COLUNAS):
                # checa cada coluna, quando a posição de uma casa é impar na sua fileira vai ser par na sua coluna e blablabla
                if coluna % 2 == ((fileira +  1) % 2):
                    if fileira < 3:
                        self.tabuleiro[fileira].append(Peca(fileira, coluna, VERMELHO))
                    elif fileira > 4:
                        self.tabuleiro[fileira].append(Peca(fileira, coluna, BRANCO))
                    else:
                        self.tabuleiro[fileira].append(0)
                else:
                    self.tabuleiro[fileira].append(0)

    def desenhar(self, janela):
        self.desenhar_quadrados(janela)
        for fileira in range(FILEIRAS):
            for coluna in range(COLUNAS):
                peca = self.tabuleiro[fileira][coluna]
                if peca != 0:
                    peca.desenhar(janela)

    def get_peca(self, fileira, coluna):
        return self.tabuleiro[fileira][coluna]

    

        


        '''for i in range(8): #8 são as quantidades de fileiras
            #P é se a casa for preta e B é se a casa for branca
            if i % 2 == 0:
                matriz.append(['b','p','b','p','b','p','b', 'p'])
            else:
                matriz.append(['p','b','p','b','p','b', 'p', 'b'])
            # eu so mudei a ordem pq tava ao contrario '''

        '''y = 0
        for largura in range(len(coluna)):
            x = 0
            for altura in range(len(altura)):
                #ele vai passar lendo cada altura e cada largura, se coincidir com o P, ele vai deixar preto e também fazer a peça vermelha
                if matriz[largura][altura] == 'p':
                    pygame.draw.rect(janela, PRETO, (x, y, TAMANHO_CASAS, TAMANHO_CASAS))
                    #tem que ter "+45" para poder ficar no centro
                    if largura <= 2:
                        pygame.draw.circle(janela, VERMELHO, (x + 45,y + 45), 30, 0)
                    elif largura >= 5:
                        pygame.draw.circle(janela, BRANCO, (x + 45,y + 45), 30, 0)
                    # gambiarra hehe
                else:
                    pygame.draw.rect(janela, BRANCO, (x, y, TAMANHO_CASAS, TAMANHO_CASAS))
                x += TAMANHO_CASAS
            y += TAMANHO_CASAS  '''


           

                    