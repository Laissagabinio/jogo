import pygame
from damas.tabuleiro import Tabuleiro
from damas.peca import Peca
from damas.constantes import BRANCO, VERMELHO, TAMANHO_CASAS

class Jogo:
    def __init__(self, janela):
        self.janela = janela 
        self._iniciar()
    
    def _iniciar(self):
        self.tabuleiro = Tabuleiro()
        self.movimentos_validos = {}
        self.selecionado = None
        self.vez = BRANCO

    def update(self):
        self.tabuleiro.desenhar(self.janela)
        self.desenhar_possibilidades(self.movimentos_validos)
        pygame.display.update()

    def reset(self):
        self._iniciar()
    
    def selecionar(self, fileira, coluna):
        if self.selecionado:
            resultado = self.mover(fileira, coluna)
            if not resultado:
                self.selecionar(fileira, coluna)
                self.selecionado = None
                
        else:
            peca = self.tabuleiro.get_peca(fileira, coluna)
            if peca != 0 and peca.cor == self.vez:
                self.selecionado = peca
                self.movimentos_validos = self.tabuleiro.movimentos_validos(peca)
                return True
            
        return False

    def desenhar_possibilidades(self, movimentos):
        for movimento in movimentos:
            fileira, coluna = movimento
            # depois eu troco esse circulo por alguma coisa mais bonita
            pygame.draw.circle(self.janela, BRANCO, (coluna * TAMANHO_CASAS + TAMANHO_CASAS//2, fileira * TAMANHO_CASAS + TAMANHO_CASAS//2), 20)

    def mover(self, fileira, coluna):
        peca = self.tabuleiro.get_peca(fileira, coluna)
        if self.selecionado and peca == 0 and (fileira, coluna) in self.movimentos_validos:
            self.tabuleiro.mover(self.selecionado, fileira, coluna)
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