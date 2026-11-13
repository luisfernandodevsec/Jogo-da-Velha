print("=== JOGO DA VELHA ===")

tabuleiro = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

for linha in tabuleiro:
    print(linha[0], "|", linha[1], "|", linha[2])

    print("--+---+--")
print("=== JOGO DA VELHA ===")

tabuleiro = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

for linha in tabuleiro:
    print(linha[0], "|", linha[1], "|", linha[2])
    print("--+---+--")

linha = int(input("Digite a linha (0 a 2): "))
coluna = int(input("Digite a coluna (0 a 2): "))

tabuleiro[linha][coluna] = "X"

print("\nTabuleiro atualizado:")
print("=== JOGO DA VELHA ===")

tabuleiro = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

jogador = "X"

for rodada in range(9):

    print("\nTabuleiro:")

    for linha in tabuleiro:
        print(linha[0], "|", linha[1], "|", linha[2])
        print("--+---+--")

    print("\nVez do jogador:", jogador)

    linha = int(input("Digite a linha (0 a 2): "))
    coluna = int(input("Digite a coluna (0 a 2): "))

    tabuleiro[linha][coluna] = jogador

    if jogador == "X":
        jogador = "O"
    else:
        jogador = "X"

print("\nFim das rodadas!")

for linha in tabuleiro:
    print(linha[0], "|", linha[1], "|", linha[2])
    print("--+---+--")
