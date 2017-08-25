#encoding: utf-8
'''----------------------------------------------------------------------
| Tarefa 4 - Implemente o Jogo da velha utilizando o algoritmo minimax	|
| 																		|
| Renan Mateus Bernardo Nascimento										|
| Vinícius Magalhães D'Assunção											|
----------------------------------------------------------------------'''

class Tabuleiro:

	tabuleiro = []			# Array 3x3 para representar o tabuleiro
	BOLA 	= 'o'
	XIS 	= 'x'
	VAZIO 	= ' '
	array_bola = []			# Possui a seguência que faz bola ser vencedor
	array_xis = []


	def __init__(self, tamanho):
		self.tamanho 	= tamanho
		self.array_bola = self.tamanho * [self.BOLA]
		self.array_xis 	= self.tamanho * [self.XIS]
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
			if self.tabuleiro[i] == array_bola:
				return self.BOLA
			if self.tabuleiro[i] == array_xis:
				return self.XIS

		return False


	def verificaColuna(self):
		for j in range(0, self.tamanho):
			if [ self.tabuleiro[i][j] for i in range(0, self.tamanho) ] == array_bola:
				return self.BOLA
			if [ self.tabuleiro[i][j] for i in range(0, self.tamanho) ] == array_xis:
				return self.XIS
		return False


	def verificaDiagonal(self):
		if [ self.tabuleiro[i][i] for i in range(0, self.tamanho) ] == array_bola:
			return self.BOLA		
		if [ self.tabuleiro[i][i] for i in range(0, self.tamanho) ] == array_xis:
			return self.XIS
		return False


	def verificaTermino(self):
		ganhouLinha = verificaLinha()
		if ganhouLinha:
			return ganhouLinha
		ganhouColuna = verificaColuna()
		if ganhouColuna:
			return ganhouColuna
		ganhouDiagonal = verificaDiagonal()
		if ganhouDiagonal:
			return ganhouDiagonal


	def imprimirTabuleiro(self):
		for i in range(0, self.tamanho):
			print(' ', end='')
			for j in range(0, self.tamanho):
				print(self.tabuleiro[i][j], end='')
				if j < self.tamanho - 1:
					print(' | ', end='')
			if i < self.tamanho - 1:
				print('\n' + (3 * self.tamanho + self.tamanho - 1) * '-')
		print (' ')