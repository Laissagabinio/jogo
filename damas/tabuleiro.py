import pygame
from .constantes import VERMELHO, PRETO, BRANCO, CINZA, FILEIRAS, COLUNAS, TAMANHO_CASAS
from .peca import Peca

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

    def mover(self, peca, fileira, coluna):
        # isso aqui é pra mover a peça sem precisar colunar numa variavel temporaria 
        self.tabuleiro[peca.fileira][peca.coluna], self.tabuleiro[fileira][coluna] = self.tabuleiro[fileira][coluna], self.tabuleiro[peca.fileira][peca.coluna]
        peca.mover(fileira, coluna)

        if fileira == 0 or fileira == FILEIRAS - 1:
            peca.torna_dama()
            if peca.cor == VERMELHO:
                self.vermelho_damas += 1
            else:
                self.branco_damas += 1

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

    def deletar_peca(self, pecas):
        for peca in pecas:
            self.tabuleiro[peca.fileira][peca.coluna] = 0
            if peca != 0:
                if peca.cor == BRANCO:
                    self.esquerda_branco -= 1
                else:
                    self.esquerda_vermelho -= 1

    
    

    def mover_direita(self, começo, fim, passo, cor, direita, pular = []):
        movimentos = {}
        ultimo = []
        for p in range(começo, fim, passo):
            if direita >= COLUNAS:
                break
            
            atual = self.tabuleiro[p][direita]
            if atual == 0:
                if pular and not ultimo:
                    break
                elif pular: 
                    movimentos[(p, direita)] = ultimo + pular 
                else:
                    movimentos[(p, direita)] = ultimo
                
                if ultimo:
                    if passo == -1:
                        fileira = max(p-3, 0)
                    else:
                        fileira = min(p+3, FILEIRAS)
                        
                    movimentos.update(self.mover_direita(p+passo, fileira, passo, cor, direita-1, pular = ultimo))
                    movimentos.update(self.mover_esquerda(p+passo, fileira, passo, cor, direita+1, pular = ultimo))
                break
            elif atual.cor == cor:
                break
            else:
                ultimo = [atual]

            direita += 1
        
        return movimentos

    def mover_esquerda(self, começo, fim, passo, cor, esquerda, pular = []):
        movimentos = {}
        ultimo = []
        for p in range(começo, fim, passo):
            if esquerda < 0:
                break
            
            atual = self.tabuleiro[p][esquerda]
            if atual == 0:
                if pular  and not ultimo:
                    break
                elif pular :
                    movimentos[(p, esquerda)] = ultimo + pular 
                else:
                    movimentos[(p, esquerda)] = ultimo
                
                if ultimo:
                    if passo == -1:
                        fileira = max(p-3, 0)
                    else:
                        fileira = min(p+3, FILEIRAS)

                    movimentos.update(self.mover_esquerda(p+passo, fileira, passo, cor, esquerda -1, pular = ultimo))
                    movimentos.update(self.mover_direita(p+passo, fileira, passo, cor, esquerda +1, pular = ultimo))
                break
            elif atual.cor == cor:
                break
            else:
                ultimo = [atual]

            esquerda -= 1
        
        return movimentos

    def movimentos_validos(self, peca):
        direita = peca.coluna + 1
        esquerda = peca.coluna - 1
        fileira = peca.fileira
        movimentos = {}

        if peca.cor == BRANCO or peca.dama:
            movimentos.update(self.mover_esquerda(fileira -1, max(fileira-3, -1), -1, peca.cor, esquerda))
            movimentos.update(self.mover_direita(fileira -1, max(fileira-3, -1), -1, peca.cor, direita))
        if peca.cor == VERMELHO or peca.dama:
            movimentos.update(self.mover_esquerda(fileira +1, min(fileira+3, FILEIRAS), 1, peca.cor, esquerda))
            movimentos.update(self.mover_direita(fileira +1, min(fileira+3, FILEIRAS), 1, peca.cor, direita))
    
        return movimentos   


           

                    