c1 = c2 = c3 = c4 = c5 = c6 = c7 = c8 = c9 = " "
jogador = "X"
jogadas = 0
venceu = False

while jogadas < 9 and not venceu:
    print()
    print(" " + c1 + " | " + c2 + " | " + c3)
    print("---+---+---")
    print(" " + c4 + " | " + c5 + " | " + c6)
    print("---+---+---")
    print(" " + c7 + " | " + c8 + " | " + c9)
    print()

    pos = int(input("Jogador " + jogador + ", escolha uma posição (1-9): "))

    if pos == 1 and c1 == " ":
        c1 = jogador
    elif pos == 2 and c2 == " ":
        c2 = jogador
    elif pos == 3 and c3 == " ":
        c3 = jogador
    elif pos == 4 and c4 == " ":
        c4 = jogador
    elif pos == 5 and c5 == " ":
        c5 = jogador
    elif pos == 6 and c6 == " ":
        c6 = jogador
    elif pos == 7 and c7 == " ":
        c7 = jogador
    elif pos == 8 and c8 == " ":
        c8 = jogador
    elif pos == 9 and c9 == " ":
        c9 = jogador
    else:
        print("Posição inválida ou já ocupada. Tente novamente.")
        continue

    jogadas += 1

    if c1 == c2 == c3 == jogador or c4 == c5 == c6 == jogador or c7 == c8 == c9 == jogador:
        venceu = True
    elif c1 == c4 == c7 == jogador or c2 == c5 == c8 == jogador or c3 == c6 == c9 == jogador:
        venceu = True
    elif c1 == c5 == c9 == jogador or c3 == c5 == c7 == jogador:
        venceu = True

    if venceu:
        print()
        print(" " + c1 + " | " + c2 + " | " + c3)
        print("---+---+---")
        print(" " + c4 + " | " + c5 + " | " + c6)
        print("---+---+---")
        print(" " + c7 + " | " + c8 + " | " + c9)
        print("\nJogador " + jogador + " venceu!")
    elif jogador == "X":
        jogador = "O"
    else:
        jogador = "X"

if not venceu:
    print("\nDeu velha! Ninguém venceu.")
