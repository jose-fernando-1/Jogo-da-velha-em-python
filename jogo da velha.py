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


def condition_diagonal(tabuleiro):
    if (tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == 'x') or (
            tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == 'x'):
        return 1
    elif (tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == 'o') or (
            tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == 'o'):
        return 2


def empate(tabuleiro, roun):
    if roun == 9:
        if condition_diagonal(tabuleiro) != 1 and condition_diagonal(tabuleiro) != 2 and condition_horizontal(
                tabuleiro) != 1 and condition_horizontal(tabuleiro) != 2 and condition_vertical(
                tabuleiro) != 1 and condition_vertical(tabuleiro) != 2:
            return True
        else:
            return False


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

        if condition_horizontal(matriz) == 1 or condition_vertical(matriz) == 1 or condition_diagonal(matriz) == 1:
            print("Player 1 ganhou!")
            print()
            imprime_tabuleiro(matriz)
            break

        if empate(matriz,roundi):
            print("Empate!")
            print()
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

        if condition_horizontal(matriz) == 2 or condition_vertical(matriz) == 2 or condition_diagonal(matriz) == 2:
            print("Player 2 ganhou!")
            print()
            imprime_tabuleiro(matriz)
            break
        roundi += 1
