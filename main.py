tab = [" "] * 9
jogador = "X"
jogadas = 0
venceu = False

while jogadas < 9 and not venceu:
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
    jogadas += 1

    combinacoes = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
    for a, b, c in combinacoes:
        if tab[a] == tab[b] == tab[c] == jogador:
            venceu = True

    if venceu:
        print()
        print(" " + tab[0] + " | " + tab[1] + " | " + tab[2])
        print("---+---+---")
        print(" " + tab[3] + " | " + tab[4] + " | " + tab[5])
        print("---+---+---")
        print(" " + tab[6] + " | " + tab[7] + " | " + tab[8])
        print("\nJogador " + jogador + " venceu!")
    else:
        if jogador == "X":
            jogador = "O"
        else:
            jogador = "X"
