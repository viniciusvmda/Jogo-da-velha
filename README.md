# Jogo da velha

Jogo da velha que utiliza o algoritmo de busca **Minimax**. 

## Pré-requisitos

* Python3

## Instruções de execução

Execute o seguinte comando no terminal:

``
python3 main.py
``

## Funcionamento

Como o jogo da velha possui um tabuleiro pequeno, foi definido que a árvore é montada e o minimax executado apenas no início do jogo.

A implementação foi feita de forma genérica quanto ao tamanho do tabuleiro, portanto, basta alterar o atributo tamanho da classe Jogo. O valor padrão é 3x3. 

Primeiro é montada a árvore do jogo, em que cada nó possui:
* As coordenadas da jogada;
* O jogador dono da jogada;
* O estado atual do tabuleiro;
* Uma lista com próximas jogadas;
* O fator de utilidade da jogada;
* E a melhor jogada dentre as próximas.

A árvore é preenchida em largura, adicionando as jogadas em um fila e desenfileirando, até a fila estar vazia. Ao chegar na folha da árvore, ou seja, não existem mais próximas jogadas (fim do jogo), é definido o fator de utilidade desta jogada que será +1 se o ganhador foi a máquina (MAX), -1 se for o humano (MIN), e 0 se houver empate.

Com a árvore pronta, a função minimax percorre a árvore em profundidade. Ao chegar à folha da árvore, sobe seu fator de utilidade para o pai da seguinte forma:
* Se o pai for MAX, ele escolhe a jogada com o maior fator de utilidade. Se houver mais de uma jogada com o maior fator de utilidade, ela escolhe a jogada que for terminal, fazendo a máquina ser a vencedora. Senão ele escolhe a jogada mais à direita. Também já é salvo índice da melhor jogada na lista de próximas jogadas.
* Se o pai for MIN, ele escolhe a jogada com o menor valor de utilidade dentre as próximas jogadas. 
* A função passa por todas as folhas da árvore para que sejam definidos os fatores de utilidade de todos os nós.

O jogo imprime as melhores jogadas para a máquina a cada rodada.