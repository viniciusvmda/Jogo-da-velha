#encoding: utf-8
'''----------------------------------------------------------------------
| Tarefa 4 - Implemente o Jogo da velha utilizando o algoritmo minimax	|
| 																		|
| Renan Mateus Bernardo Nascimento										|
| Vinícius Magalhães D'Assunção											|
----------------------------------------------------------------------'''

class Jogada:
    # Enum de utilidades
    MAX = 1
    MED = 0
    MIN = -1


    def __init__(self, tabuleiro, jogada, jogador, ant):
        self.jogada = jogada                # tupla contendo as coordenadas da jogada
        self.jogador = jogador              # jogador dono da jogada
        self.tabuleiro = tabuleiro          # estado atual do tabuleiro
        self.ant = ant                      # instância da jogada anterior
        self.prox = []                      # lista com próximas jogadas
        self.utilidade = self.MED


    '''
        Adiciona jogada a lista de próximas jogadas
    '''
    def adicionarProximaJogada(self, jogada):
        self.prox.append(jogada)

    '''
        Define MAX se jogador ganhou, MIN se perdeu, MED caso empate 
    '''
    def adicionarUtilidade(self, utilidade):
        self.utilidade = utilidade