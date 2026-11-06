tab = [" "] * 9
jogador = "X"

while True:
    print()
    print(" " + tab[0] + " | " + tab[1] + " | " + tab[2])
    print("---+---+---")
    print(" " + tab[3] + " | " + tab[4] + " | " + tab[5])
    print("---+---+---")
    print(" " + tab[6] + " | " + tab[7] + " | " + tab[8])
    print()

    pos = int(input("Jogador " + jogador + ", escolha uma posição (1-9): ")) - 1

    if pos < 0 or pos > 8 or tab[pos] != " ":
        print("Posição inválida ou já ocupada. Tente novamente.")
        continue

    tab[pos] = jogador

    if jogador == "X":
        jogador = "O"
    else:
        jogador = "X"
