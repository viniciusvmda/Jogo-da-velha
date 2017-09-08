#encoding: utf-8
'''----------------------------------------------------------------------
| Tarefa 4 - Implemente o Jogo da velha utilizando o algoritmo minimax	|
| 																		|
| Renan Mateus Bernardo Nascimento										|
| Vinícius Magalhães D'Assunção											|
----------------------------------------------------------------------'''

class Tabuleiro:
	# Atributos estáticos
	BOLA 	= 'o'
	XIS 	= 'x'
	VAZIO 	= ' '
	EMPATE 	= '='
	
	
	def __init__(self, tamanho):
		# Tamanho do tabuleiro
		self.tamanho 	= tamanho
		# Possui a sequência que faz bola ser vencedor
		self.array_bola = self.tamanho * [self.BOLA]
		# Possui a sequência que faz xis ser vencedor
		self.array_xis 	= self.tamanho * [self.XIS]
		# Array 3x3 para representar o tabuleiro
		self.tabuleiro = [ self.tamanho * [self.VAZIO] for i in range(0, self.tamanho) ]


	# Colocar vazio em todas as posições do tabuleiro
	def limpaTabuleiro(self):
		self.tabuleiro = [ self.tamanho * [self.VAZIO] for i in range(0, self.tamanho) ]


	def marcaBola(self, x, y):
		self.tabuleiro[x][y] = self.BOLA


	def marcaXis(self, x, y):
		self.tabuleiro[x][y] = self.XIS


	def verificaLinha(self):
		for i in range(0, self.tamanho):
			if self.tabuleiro[i] == self.array_bola:
				return self.BOLA
			if self.tabuleiro[i] == self.array_xis:
				return self.XIS
		return False


	def verificaColuna(self):
		for j in range(0, self.tamanho):
			if [ self.tabuleiro[i][j] for i in range(0, self.tamanho) ] == self.array_bola:
				return self.BOLA
			if [ self.tabuleiro[i][j] for i in range(0, self.tamanho) ] == self.array_xis:
				return self.XIS
		return False


	def verificaDiagonal(self):
		# Verifica diagonal principal
		if [ self.tabuleiro[i][i] for i in range(0, self.tamanho) ] == self.array_bola:
			return self.BOLA		
		if [ self.tabuleiro[i][i] for i in range(0, self.tamanho) ] == self.array_xis:
			return self.XIS
		
		# Verifica diagonal secundária
		t = self.tamanho - 1
		if [ self.tabuleiro[i][t - i] for i in range(0, self.tamanho) ] == self.array_bola:
			return self.BOLA
		if [ self.tabuleiro[i][t - i] for i in range(0, self.tamanho) ] == self.array_xis:
			return self.XIS

		return False


	def verificaEmpate(self):
		for i in range(0, self.tamanho):
			for j in range(0, self.tamanho):
				if self.tabuleiro[i][j] == self.VAZIO:
					return False
		return self.EMPATE


	'''
		Retorna o jogador vencedor ou False se não houve ganhador
	'''
	def ganhou(self):
		ganhouLinha = self.verificaLinha()
		if ganhouLinha:
			return ganhouLinha
		ganhouColuna = self.verificaColuna()
		if ganhouColuna:
			return ganhouColuna
		ganhouDiagonal = self.verificaDiagonal()
		if ganhouDiagonal:
			return ganhouDiagonal
		empate = self.verificaEmpate()
		return empate


	def imprimirTabuleiro(self):
		print()
		for i in range(0, self.tamanho):
			print(' ', end='')
			for j in range(0, self.tamanho):
				print(self.tabuleiro[i][j], end='')
				if j < self.tamanho - 1:
					print(' | ', end='')
			if i < self.tamanho - 1:
				print('\n' + (3 * self.tamanho + self.tamanho - 1) * '-')
		print(' ')