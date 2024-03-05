def imprime_tabuleiro(tabuleiro):
    for linhas in tabuleiro:
        print(" ".join(linhas))


def inicializa_tabuleiro():
    matriz = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]
    return matriz


imprime_tabuleiro(inicializa_tabuleiro())  # Imprime o tabuleiro vazio