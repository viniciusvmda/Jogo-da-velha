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
    VAZIO = -2


    def __init__(self, tabuleiro, jogada, jogador):
        self.jogada = jogada                # tupla contendo as coordenadas da jogada
        self.jogador = jogador              # jogador dono da jogada
        self.tabuleiro = tabuleiro          # estado atual do tabuleiro
        self.prox = []                      # lista com próximas jogadas
        self.utilidade = self.VAZIO         # fator de utilidade da jogada
        self.melhor_escolha = -2            # armazena o índice da melhor jogada entre as próximas 


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