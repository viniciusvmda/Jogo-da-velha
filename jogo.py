#encoding: utf-8
'''----------------------------------------------------------------------
| Tarefa 4 - Implemente o Jogo da velha utilizando o algoritmo minimax	|
| 																		|
| Renan Mateus Bernardo Nascimento										|
| Vinícius Magalhães D'Assunção											|
----------------------------------------------------------------------'''

from Tabuleiro import Tabuleiro

class Jogo:

	tabuleiro = None
	arvore = []

	def __init__(self):
		self.tabuleiro = Tabuleiro()

	def montaArovre(self,)