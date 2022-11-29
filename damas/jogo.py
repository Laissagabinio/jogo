import pygame
from .tabuleiro import Tabuleiro
from .peca import Peca
from .constantes import BRANCO, VERMELHO, TAMANHO_CASAS


# essa classe vai servir pra colocar a IA depois sem precisar de algum input 
class Jogo:
    def __init__(self, janela):
        self.janela = janela
        self._iniciar()
             
    def update(self):
        self.tabuleiro.desenhar(self.janela)
        self.desenhar_possibilidades(self.movimentos_validos)
        pygame.display.update()
    
    def _iniciar(self):
        self.selecionado = None
        self.tabuleiro = Tabuleiro()      
        self.vez = BRANCO
        self.movimentos_validos = {}

    def reset(self):
        self._iniciar()
    
    def selecionar(self, fileira, coluna):
        if self.selecionado:
            resultado = self._mover(fileira, coluna)
            if not resultado:
                # o resultado vai ser falso quando algo q nao seja uma peça for selecionado   
                self.selecionado = None
                # chama o metodo selecionar de novo, assim o jogo nao para quando uma peça nao for selecionada
                self.selecionar(fileira, coluna)
        #else        
        else:
            peca = self.tabuleiro.get_peca(fileira, coluna)
            if peca != 0 and peca.cor == self.vez:
                self.selecionado = peca
                self.movimentos_validos = self.tabuleiro.get_movimentos_validos(peca)
                return True
                # retorna se a seleção é valida
            
        return False

    def desenhar_possibilidades(self, movimentos):
        for movimento in movimentos:
            fileira, coluna = movimento
            # depois eu troco esse circulo por alguma coisa mais bonita
            pygame.draw.circle(self.janela, BRANCO, (coluna * TAMANHO_CASAS + TAMANHO_CASAS//2, fileira * TAMANHO_CASAS + TAMANHO_CASAS//2), 15)

    def _mover(self, fileira, coluna):
        peca = self.tabuleiro.get_peca(fileira, coluna)
        if self.selecionado and peca == 0 and (fileira, coluna) in self.movimentos_validos:
            self.tabuleiro.mover(self.selecionado, fileira, coluna) # self.selecionado diz a posição da peça e fileira, coluna pra onde a peça vai ser movida
            pular = self.movimentos_validos[(fileira, coluna)]
    
            if pular:
                self.tabuleiro.deletar_peca(pular)
            self.mudar_vez()
        else:
            return False

        return True

    def mudar_vez(self):
        self.movimentos_validos = {}
        if self.vez == BRANCO:
            self.vez = VERMELHO
        else:
            self.vez = BRANCO

    '''def deletar_peca(self, pecas):
        for peca in pecas:
            self.tabuleiro[peca.fileira][peca.coluna] = 0'''

    