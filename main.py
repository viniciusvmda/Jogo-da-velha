#encoding: utf-8
'''----------------------------------------------------------------------
| Tarefa 4 - Implemente o Jogo da velha utilizando o algoritmo minimax	|
| 																		|
| Renan Mateus Bernardo Nascimento										|
| Vinícius Magalhães D'Assunção											|
----------------------------------------------------------------------'''

from tabuleiro import Tabuleiro
from jogo import Jogo


# Lê parâmetros para o jogo do usuário
jogador = input('Escolha entre (' + Tabuleiro.XIS + ') e (' + Tabuleiro.BOLA + '): ')
while jogador != Tabuleiro.XIS and jogador != Tabuleiro.BOLA:
    print('Valor inválido!')
    jogador = input('Escolha entre (' + Tabuleiro.XIS + ') e (' + Tabuleiro.BOLA + '): ')

jogo_velha = Jogo(jogador)
jogo_velha.jogar()