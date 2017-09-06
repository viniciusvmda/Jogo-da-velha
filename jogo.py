#encoding: utf-8
'''----------------------------------------------------------------------
| Tarefa 4 - Implemente o Jogo da velha utilizando o algoritmo minimax	|
| 																		|
| Renan Mateus Bernardo Nascimento										|
| Vinícius Magalhães D'Assunção											|
----------------------------------------------------------------------'''

import copy
from tabuleiro import Tabuleiro
from jogada import Jogada

class Jogo:

	def __init__(self, tamanho, jogador):
		self.tamanho = tamanho												# tamanho do tabuleiro
		self.jogador = jogador              								# jogador dono da jogada
		self.tabuleiro = Tabuleiro(tamanho)									# tabuleiro do jogo, alterado a cada jogada
		self.arvore = Jogada(self.tabuleiro, None, self.jogador, None)		# arvore de jogadas


	def montaArvore(self):
		# fila para preenchimento em largura
		fila = [self.arvore]
		# Enquanto a fila não estiver vazia
		while fila:
			# Desenfileira
			jogada_atual = fila.pop(0)
			# Adiciona todas as jogadas possíveis como próximas da jogada atual
			for i in range(0, self.tamanho):
				for j in range(0, self.tamanho):
					# se posicao estiver vazia
					if jogada_atual.tabuleiro.tabuleiro[i][j] == Tabuleiro.VAZIO:
						# Cria uma copia do tabuleiro atual
						proximo_tabuleiro = copy.deepcopy(jogada_atual.tabuleiro)
						# Preenhce o proximo tabuleiro com a proxima jogada
						proximo_jogador = Tabuleiro.BOLA
						if jogada_atual.jogador == Tabuleiro.XIS:
							proximo_tabuleiro.marcaXis(i, j)
						else:
							proximo_tabuleiro.marcaBola(i, j)
							proximo_jogador = Tabuleiro.XIS
						proxima_jogada = Jogada(proximo_tabuleiro, (i,j), proximo_jogador, jogada_atual)
						jogada_atual.adicionarProximaJogada(proxima_jogada)
						# Verifica se o jogo terminou
						ganhou = proxima_jogada.tabuleiro.ganhou()
						if not ganhou:
							# Enfileira proxima jogada
							fila.append(proxima_jogada)
						else:
							if ganhou == self.jogador:
								proxima_jogada.adicionarUtilidade(Jogada.MAX)
							elif ganhou == Tabuleiro.EMPATE:
								proxima_jogada.adicionarUtilidade(Jogada.MED)
							else:
								proxima_jogada.adicionarUtilidade(Jogada.MIN)


	def imprimeArvore(self):
		# fila para preenchimento em largura
		fila = [self.arvore]
		# Enquanto a fila não estiver vazia
		while fila:
			jogada_atual = fila.pop(0)
			jogada_atual.tabuleiro.imprimirTabuleiro()
			fila += jogada_atual.prox
			if not len(jogada_atual.prox):
				print("terminou")
			print("\n\n")