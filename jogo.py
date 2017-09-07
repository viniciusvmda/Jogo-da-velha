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
		self.jogador = jogador              								# peça correspondente ao jogador
		self.maquina = Tabuleiro.XIS										# peça correspondente à jogador

		if jogador == Tabuleiro.XIS:
			self.maquina = Tabuleiro.BOLA
		
		self.tabuleiro = Tabuleiro(tamanho)									# tabuleiro do jogo, alterado a cada jogada
		self.arvore = Jogada(self.tabuleiro, None, self.maquina, None)		# arvore de jogadas


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
							# Se o jogo terminou adiciona utilidade à jogada
							if ganhou == self.maquina:
								proxima_jogada.adicionarUtilidade(Jogada.MAX)
							elif ganhou == Tabuleiro.EMPATE:
								proxima_jogada.adicionarUtilidade(Jogada.MED)
							else:
								proxima_jogada.adicionarUtilidade(Jogada.MIN)



	'''
		Percorre a árvore em profundidade
		Para ao chegar à folha da árvore, subindo seu fator de utilidade para o pai
		Se o pai for max, ele escolhe o maior, senão, ele escolhe o min
		Deve passar por todas as folhas da árvore para que sejam definidos os fatores de utilidade das mesmas
	'''
	def minimax(self, jogada):
		# Se não houver próximas jogadas, jogada é uma folha
		if not len(jogada.prox):
			# Retorna utilidade da jogada 
			return jogada.utilidade

		# Percorre as próximas jogada
		for proxima in jogada.prox:
			# Pega a utilidade da próxima jogada
			utilidade = self.minimax(proxima)
			# Se o jogador for o computador, faz o max da utilidade, senão faz o min
			if jogada.jogador == self.maquina:
				jogada.utilidade = max(jogada.utilidade, utilidade)
			else:
				jogada.utilidade = min(jogada.utilidade, utilidade)
		
		return jogada.utilidade


	def jogar(self):
		self.montaArvore()
		self.minimax(self.arvore)
		
		vez = self.maquina
		proxima_vez = self.jogador
		jogada = self.arvore
		ganhou = False

		while not ganhou:
			x, y = 0, 0
			if vez == self.maquina:
				i = self.lerJogadaMaquina(jogada)
				jogada = jogada.prox[i]
				x, y = jogada.jogada
				proxima_vez = self.jogador
			else:
				x, y = self.lerJogadaHumano()
				for proxima in jogada.prox:
					if proxima.jogada == (x,y):
						jogada = proxima
						break
				proxima_vez = self.maquina

			self.tabuleiro.tabuleiro[x][y] = vez
			aux = vez
			vez = proxima_vez
			proxima_vez = aux
			ganhou = self.tabuleiro.ganhou()
		
		print('Jogador (' + ganhou + ') venceu!')

		
	def lerJogadaHumano(self):
		self.tabuleiro.imprimirTabuleiro()
		x, y = input('Sua vez (x,y): ').split(',')
		x, y = int(x), int(y)
		while x < 0 and x >= self.tamanho and y < 0 and y >= self.tamanho and self.tabuleiro.tabuleiro[x][y] != Tabuleiro.VAZIO:
			print('Valor inválido!')
			x, y = input('Sua vez (x,y): ').split(',')
			x, y = int(x), int(y)
		return x, y

	
	'''
		Retorna o índice da lista de próximas jogadas da jogada recebida com a maior utilidade 
	'''
	def lerJogadaMaquina(self, jogada):
		maior = 0				# salva o índice da jogada de maior utilidade
		for i, proxima in enumerate(jogada.prox[1:]):
			if proxima.utilidade > jogada.prox[maior].utilidade:
				maior = i + 1	# soma 1 pois começa o loop do segundo elemento	
		return maior
	

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