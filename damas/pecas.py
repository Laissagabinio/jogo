import pygame
from .constantes import PRETO, BRANCO, VERMELHO, FILEIRAS, COLUNAS, TAMANHO_CASAS


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

    def movimento(self, coluna, fileira):
        self.coluna = coluna
        self.fileira = fileira 
        self.posição()

    def movimentos_validos(self, peca):
        movimentos = {}
        direita = peca.coluna + 1
        esquerda = peca.coluna - 1
        fileira = peca.fileira

        if peca.cor == BRANCO or peca.dama:
            movimentos.update(self._traverse_esquerda(fileira -1, max(fileira-3, -1), -1, peca.cor, esquerda))
            movimentos.update(self._traverse_direita(fileira -1, max(fileira-3, -1), -1, peca.cor, direita))
        if peca.cor == VERMELHO or peca.dama:
            movimentos.update(self._traverse_esquerda(fileira +1, min(fileira+3, FILEIRAS), 1, peca.cor, esquerda))
            movimentos.update(self._traverse_direita(fileira +1, min(fileira+3, FILEIRAS), 1, peca.cor, direita))
        
        return movimentos

    def mover_direita(self, começo, fim, cor, direita, passo, pular = []):
        movimentos = {}
        ultimo = []
        for p in range(começo, fim, passo):
            if direita >= COLUNAS:
                break
            
            atual = self.tabuleiro[p][direita]
            if atual == 0:
                if pular and not ultimo:
                    break
                elif pular : 
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

    def mover_esquerda(self, começo, fim, cor, esquerda, passo, pular = []):
        movimentos = {}
        ultimo = []
        for p in range(começo, fim, passo):
            if esquerda < 0:
                break
            
            atual = self.board[p][esquerda]
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

                    movimentos.update(self.mover_esquerda(p+passo, fileira, passo, cor, esquerda-1, pular = ultimo))
                    movimentos.update(self.mover_direita(p+passo, fileira, passo, cor, esquerda+1, pular = ultimo))
                break
            elif atual.cor == cor:
                break
            else:
                ultimo = [atual]

            esquerda -= 1
        
        return movimentos


    def desenhar_possibilidades(self, movimentos):
        for movimento in movimentos:
            fileira, coluna = movimento
            # depois eu troco esse circulo por alguma coisa mais bonita
            pygame.draw.circle(self.janela, BRANCO, (coluna * TAMANHO_CASAS + TAMANHO_CASAS//2, fileira * TAMANHO_CASAS + TAMANHO_CASAS//2), 20)



        '''peça_vermelha = pygame.draw.circle(janela, VERMELHO, (self.x,self.y), 15, 0)
        peça_branca = pygame.draw.circle(janela, BRANCO, (self.x,self.y), 15, 0)'''
''' for fileira in range(FILEIRAS):
            #esse fileira%2 serve pra fazer dois tipos de padrões,
            #um começando com branco, q vale 0 e outro preto valendo 1, quando usa %2 desenha a cada duas casas
            for coluna in range(fileira % 2, FILEIRAS, 2):
                if fileira%2 == 1:
                    pygame.draw.circle(janela, VERMELHO, (fileira * TAMANHO_CASAS-(TAMANHO_CASAS /2), coluna * (TAMANHO_CASAS) /2),10)
                else:
                    break'''
                



