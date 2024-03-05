def imprime_tabuleiro(tabuleiro):
    for linhas in tabuleiro:
        print(" ".join(linhas))


matriz = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]


def condition_horizontal(tabuleiro):
    for linhas in tabuleiro:
        if linhas[0] == linhas[1] == linhas[2] == 'x':
            return 1
        elif linhas[0] == linhas[1] == linhas[2] == 'o':
            return 2


def condition_vertical(tabuleiro):
    for coluna in range(3):
        if tabuleiro[0][coluna] == tabuleiro[1][coluna] == tabuleiro[2][coluna] == 'x':
            return 1
        elif tabuleiro[0][coluna] == tabuleiro[1][coluna] == tabuleiro[2][coluna] == 'o':
            return 2



roundi = 1
while roundi < 10:
    if roundi % 2 != 0:
        print("Player 1 joga")
        print()
        imprime_tabuleiro(matriz)
        print()
        print("1-9")
        print()
        escolha = int(input())
        if escolha == 1 or escolha == 2 or escolha == 3:
            matriz[0][escolha - 1] = 'x'
        elif escolha == 4 or escolha == 5 or escolha == 6:
            matriz[1][escolha - 4] = 'x'
        elif escolha == 7 or escolha == 8 or escolha == 9:
            matriz[2][escolha - 7] = 'x'

        if condition_horizontal(matriz) == 1 or condition_vertical(matriz) == 1:
            print("Player 1 ganhou!")
            break
        roundi += 1
    else:
        print("Player 2 joga")
        print()
        imprime_tabuleiro(matriz)
        print()
        print("1-9")
        print()
        escolha = int(input())
        if escolha == 1 or escolha == 2 or escolha == 3:
            matriz[0][escolha - 1] = 'o'
        elif escolha == 4 or escolha == 5 or escolha == 6:
            matriz[1][escolha - 4] = 'o'
        elif escolha == 7 or escolha == 8 or escolha == 9:
            matriz[2][escolha - 7] = 'o'

        if condition_horizontal(matriz) == 2 or condition_vertical(matriz) == 2:
            print("Player 2 ganhou!")
            break
        roundi += 1


