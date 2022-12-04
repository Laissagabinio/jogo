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
        tamanho_texto = 22
        fonte = pygame.font.Font('assets/Copperplate_Gothic_Light.ttf', tamanho_texto)

        turno = fonte.render('Turno: ', True, (PRETO))
        janela.blit(turno, (730, 500))
        
         
        for fileira in range(FILEIRAS):
            #esse fileira%2 serve pra fazer dois tipos de padrões,
            #um começando com branco, q vale 0 e outro preto valendo 1, quando usa %2 desenha a cada duas casas
            for coluna in range(fileira % 2, FILEIRAS, 2):
                pygame.draw.rect(janela, BRANCO, (fileira * TAMANHO_CASAS, coluna * TAMANHO_CASAS, TAMANHO_CASAS, TAMANHO_CASAS))
        #pygame.display.update()

    def criar_tabuleiro(self):
    
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
                        # aqui onde nao tem uma peça ele adiciona 0
                        self.tabuleiro[fileira].append(0)
                else:
                    self.tabuleiro[fileira].append(0)

    def desenhar(self, janela):
        self.desenhar_quadrados(janela)
        for fileira in range(FILEIRAS):
            for coluna in range(COLUNAS):
                peca = self.tabuleiro[fileira][coluna]
                # a peça é 0 onde nao tem peças
                if peca != 0:
                    peca.desenhar(janela)

    def mover(self, peca, fileira, coluna):
        # isso aqui é pra mover a peça sem precisar colocar numa variavel temporaria 
        self.tabuleiro[peca.fileira][peca.coluna], self.tabuleiro[fileira][coluna] = self.tabuleiro[fileira][coluna], self.tabuleiro[peca.fileira][peca.coluna]
        peca.mover(fileira, coluna)

        if fileira == 0 or fileira == FILEIRAS - 1:
            peca.torna_dama()
            if peca.cor == VERMELHO:
                self.vermelho_damas += 1
            else:
                self.branco_damas += 1

    def get_peca(self, fileira, coluna):
        return self.tabuleiro[fileira][coluna]

    def get_movimentos_validos(self, peca):
        # os movimentos validos vao ficar dentro desse dicionario
        movimentos = {}
        direita = peca.coluna + 1
        esquerda = peca.coluna - 1
        fileira = peca.fileira   

        if peca.cor == BRANCO or peca.dama:
            movimentos.update(self._mover_esquerda(fileira -1, max(fileira-3, -1), -1, peca.cor, esquerda))
            movimentos.update(self._mover_direita(fileira -1, max(fileira-3, -1), -1, peca.cor, direita))
        if peca.cor == VERMELHO or peca.dama:
            movimentos.update(self._mover_esquerda(fileira +1, min(fileira+3, FILEIRAS), 1, peca.cor, esquerda))
            movimentos.update(self._mover_direita(fileira +1, min(fileira+3, FILEIRAS), 1, peca.cor, direita))
    
        return movimentos

    def _mover_direita(self, começo, fim, passo, cor, direita, pular = []):
        movimentos = {}
        ultimo = []
        for f in range(começo, fim, passo):
            if direita >= COLUNAS:
                break
            
            # esse f é outra variavel pra fileira
            atual = self.tabuleiro[f][direita]
            if atual == 0:
                # vai ser 0 quando uma casa estiver vazia
                if pular and not ultimo:
                    # aqui ele chega se se alguma peça foi comida e nao tem outra possibilidade, entao ele encerra a jogada 
                    break
                elif pular: 
                    # aqui serve pra ele comer duas peças ao mesmo tempo
                    movimentos[(f, direita)] = ultimo + pular 
                else:
                    movimentos[(f, direita)] = ultimo
                
                if ultimo:
                    if passo == -1:
                        fileira = max(f-3, 0)
                    else:
                        fileira = min(f+3, FILEIRAS)
                        
                    movimentos.update(self._mover_direita(f+passo, fileira, passo, cor, direita-1, pular = ultimo))
                    movimentos.update(self._mover_esquerda(f+passo, fileira, passo, cor, direita+1, pular = ultimo))
                break
            elif atual.cor == cor:
                break
            else:
                ultimo = [atual]

            direita += 1
        
        return movimentos

    def _mover_esquerda(self, começo, fim, passo, cor, esquerda, pular = []):
        movimentos = {}
        ultimo = []
        for f in range(começo, fim, passo):
            if esquerda != 0 and esquerda < 0:
                break
            
            atual = self.tabuleiro[f][esquerda]
            if atual == 0:
                if pular and not ultimo:
                    break
                elif pular:
                    movimentos[(f, esquerda)] = ultimo + pular 
                else:
                    movimentos[(f, esquerda)] = ultimo
                
                if ultimo:
                    if passo == -1:
                        fileira = max(f-3, 0)
                    else:
                        fileira = min(f+3, FILEIRAS)

                    movimentos.update(self._mover_esquerda(f+passo, fileira, passo, cor, esquerda -1, pular = ultimo))
                    movimentos.update(self._mover_direita(f+passo, fileira, passo, cor, esquerda +1, pular = ultimo))
                break
            elif atual.cor == cor:
                break
            else:
                ultimo = [atual]

            esquerda -= 1
        
        return movimentos

    def deletar_peca(self, pecas):
        for peca in pecas:
            self.tabuleiro[peca.fileira][peca.coluna] = 0
            if peca != 0:
                if peca.cor == BRANCO:
                    self.branco_peças -= 1
                else:
                    self.vermelho_peças -= 1

           

                    