import random

tabuleiro = []

for i in range(3):
    linha = []
    for j in range(3):
        linha.append(" ")
    tabuleiro.append(linha)

def mostraTabuleiro():
    for i in range(3):
        print(tabuleiro[i][0] + " | " + tabuleiro[i][1] + " | " + tabuleiro[i][2])
        if i != 2:
           print("-" * 10)

def verificaVitoria(jogador): 
    for i in range(3):
        if tabuleiro[i][0] == jogador and tabuleiro[i][1] == jogador and tabuleiro[i][2] == jogador:
            return True
    for i in range(3):
        if tabuleiro[0][i] == jogador and tabuleiro[1][i] == jogador and tabuleiro[2][i] == jogador:
            return True
    if tabuleiro[0][0] == jogador and tabuleiro[1][1] == jogador and tabuleiro[2][2] == jogador:
        return True
    if tabuleiro[0][2] == jogador and tabuleiro[1][1] == jogador and tabuleiro[2][0] == jogador:
        return True

    return False

def fazJogada(jogador):
    while (True):
        chuteL = int(input("linha: ")) - 1
        chuteC = int(input("coluna: ")) - 1

        if tabuleiro[chuteL][chuteC] == " ":
            tabuleiro[chuteL][chuteC] = jogador
            return

        print("Jogada inválida!")

def computadorJoga():
    while (True):
        chuteL = random.randrange(3)
        chuteC = random.randrange(3)

        if tabuleiro[chuteL][chuteC] == " ":
            tabuleiro[chuteL][chuteC] = "O"
            return

qtdJogadores = 0

while qtdJogadores not in [1, 2]:
    qtdJogadores = int(input("Quantos jogadores? (1 ou 2): "))
jogadas = 0

while (True):
    mostraTabuleiro()
    fazJogada("X")
    jogadas += 1

    if verificaVitoria("X"):
        mostraTabuleiro()
        print("Jogador X venceu!")
        break

    if jogadas == 9:
        mostraTabuleiro()
        print("Empate!")
        break

    if qtdJogadores == 2:
        mostraTabuleiro()
        fazJogada("O")
    else:
        computadorJoga()
    jogadas += 1

    if verificaVitoria("O"):
        mostraTabuleiro()
        print("Jogador O venceu!")
        break