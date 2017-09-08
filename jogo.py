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
from random import randrange


class Jogo:

	def __init__(self, jogador):
		self.tamanho = 3												# tamanho do tabuleiro 3x3
		self.jogador = jogador              							# peça correspondente ao jogador
		self.maquina = Tabuleiro.XIS									# peça correspondente à jogador

		if jogador == Tabuleiro.XIS:
			self.maquina = Tabuleiro.BOLA
		
		self.tabuleiro = Tabuleiro(self.tamanho)						# tabuleiro do jogo, alterado a cada jogada
		self.arvore = Jogada(self.tabuleiro, None, self.maquina)		# arvore de jogadas


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
						
						# Preenche o proximo tabuleiro com a proxima jogada
						proximo_jogador = Tabuleiro.BOLA
						if jogada_atual.jogador == Tabuleiro.XIS:
							proximo_tabuleiro.marcaXis(i, j)
						else:
							proximo_tabuleiro.marcaBola(i, j)
							proximo_jogador = Tabuleiro.XIS
						
						proxima_jogada = Jogada(proximo_tabuleiro, (i,j), proximo_jogador)
						jogada_atual.adicionarProximaJogada(proxima_jogada)
						
						# Verifica se o jogo terminou com a próxima jogada
						ganhou = proxima_jogada.tabuleiro.ganhou()
						if not ganhou:
							# Enfileira proxima jogada
							fila.append(proxima_jogada)
						else:
							# Adiciona utilidade à jogada
							if ganhou == self.maquina:			# Máquina venceu
								proxima_jogada.adicionarUtilidade(Jogada.MAX)
							elif ganhou == Tabuleiro.EMPATE:	# Empate
								proxima_jogada.adicionarUtilidade(Jogada.MED)
							else:								# Humano venceu
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
		
		melhor = 0			# salva o índice da jogada de melhor utilidade
		ganhou = -1			# salva o índice da jogada que ganhou o jogo

		# Percorre as próximas jogadas
		for i, proxima in enumerate(jogada.prox):
			# Pega a utilidade da próxima jogada
			utilidade = self.minimax(proxima)
			# Se o jogador for o computador, faz o max da utilidade, senão faz o min
			if jogada.jogador == self.maquina:
				if jogada.utilidade != Jogada.VAZIO: 
					jogada.utilidade = max(jogada.utilidade, utilidade)
				else:
					jogada.utilidade = utilidade

				if utilidade >= jogada.prox[melhor].utilidade:
					melhor = i
					# Verifica se esta jogada ganha o jogo
					if utilidade == Jogada.MAX and not len(proxima.prox):
						ganhou = i
			else:
				if jogada.utilidade != Jogada.VAZIO: 
					jogada.utilidade = min(jogada.utilidade, utilidade)
				else:
					jogada.utilidade = utilidade
		
		if jogada.jogador == self.maquina:
			# Salva a melhor escolha da jogada
			if ganhou > -1:
				jogada.melhor_escolha = ganhou
			else:
				jogada.melhor_escolha = melhor

		return jogada.utilidade


	'''
		Monta a árvore antes e utiliza o minimax antes de iniciar a partida
		Alterna a vez da jogada entre máquina e humano até a partida terminar
	'''
	def jogar(self):
		vez = self.maquina			# Guarda quem é o jogador da vez
		proxima_vez = self.jogador	# Guarda quem será o próximo a jogar
		ganhou = False				# Variável auxiliar para informar se a partida acabou
		
		# Decide quem irá começar primeiro
		moeda = randrange(2)
		if moeda:
			print('\nMáquina começa primeiro.')
		else:
			x, y = self.lerJogadaHumano()
			self.tabuleiro.tabuleiro[x][y] = self.jogador
			self.arvore = Jogada(self.tabuleiro, (x, y), self.maquina)
			vez = self.maquina
			proxima_vez = self.jogador
		
		jogada = self.arvore		# Ponteiro para a jogada atual na árvore
		self.montaArvore()
		jogada.utilidade = self.minimax(self.arvore)
		while not ganhou:
			x, y = 0, 0
			if vez == self.maquina:
				# Retorna o índice da próxima jogada da máquina com maior valor de utilidade
				i = jogada.melhor_escolha
				# Move o ponteiro para esta jogada
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

			# Marca o tabuleiro com a jogada do turno
			self.tabuleiro.tabuleiro[x][y] = vez
			# Altera o jogador do turno
			aux = vez
			vez = proxima_vez
			proxima_vez = aux
			ganhou = self.tabuleiro.ganhou()
		
		self.imprimirGanhador(ganhou)
		

	'''
		Lê do usuário as coordenadas da próxima jogada e as retorna
	'''
	def lerJogadaHumano(self):
		self.tabuleiro.imprimirTabuleiro()
		x, y = input('\nSua vez jogador (' + self.jogador + '). Entre com as coordenadas no formato x,y: ').split(',')
		x, y = int(x), int(y)
		while x < 0 or x >= self.tamanho or y < 0 or y >= self.tamanho or self.tabuleiro.tabuleiro[x][y] != Tabuleiro.VAZIO:
			print('\nValor inválido!')
			x, y = input('\nSua vez jogador (' + self.jogador + '). Entre com as coordenadas no formato x,y: ').split(',')
			x, y = int(x), int(y)
		return x, y
	

	def imprimirGanhador(self, ganhou):
		self.tabuleiro.imprimirTabuleiro()
		if ganhou == Tabuleiro.EMPATE:
			print('\nJogo empatado!')
		else:
			print('\nJogador (' + ganhou + ') venceu!')


	def imprimirArvore(self):
		self.montaArvore()
		self.minimax(self.arvore)
		# fila para preenchimento em largura
		fila = [self.arvore]
		# Enquanto a fila não estiver vazia
		while fila:
			jogada_atual = fila.pop(0)
			jogada_atual.tabuleiro.imprimirTabuleiro()
			fila += jogada_atual.prox
			print('Utilidade: ' + str(jogada_atual.utilidade))
			if not len(jogada_atual.prox):
				print("terminou")
			print("\n\n")