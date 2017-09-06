#encoding: utf-8
'''----------------------------------------------------------------------
| Tarefa 4 - Implemente o Jogo da velha utilizando o algoritmo minimax	|
| 																		|
| Renan Mateus Bernardo Nascimento										|
| Vinícius Magalhães D'Assunção											|
----------------------------------------------------------------------'''

from tabuleiro import Tabuleiro
from jogo import Jogo

jogo_velha = Jogo(3, Tabuleiro.XIS)
jogo_velha.montaArvore()
jogo_velha.imprimeArvore()