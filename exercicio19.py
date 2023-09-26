def imprimir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(" | ".join(linha))
        print("-" * 9)

def verificar_vitoria(tabuleiro, jogador):
    for i in range(3):
        if all(tabuleiro[i][j] == jogador for j in range(3)) or \
           all(tabuleiro[j][i] == jogador for j in range(3)):
            return True
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == jogador or \
       tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == jogador:
        return True
    return False

def jogo_da_velha():
    tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
    jogador_atual = "X"

    for _ in range(9):  
        imprimir_tabuleiro(tabuleiro)
        print(f"Jogador {jogador_atual}, é a sua vez!")

        while True:
            try:
                linha = int(input("Informe a linha (0, 1 ou 2): "))
                coluna = int(input("Informe a coluna (0, 1 ou 2): "))
                if 0 <= linha <= 2 and 0 <= coluna <= 2 and tabuleiro[linha][coluna] == " ":
                    break
                else:
                    print("Jogada inválida. Tente novamente.")
            except ValueError:
                print("Entrada inválida. Informe números inteiros.")

        tabuleiro[linha][coluna] = jogador_atual

        if verificar_vitoria(tabuleiro, jogador_atual):
            imprimir_tabuleiro(tabuleiro)
            print(f"Parabéns, jogador {jogador_atual}! Você venceu!")
            break

        jogador_atual = "O" if jogador_atual == "X" else "X"
    else:
        imprimir_tabuleiro(tabuleiro)
        print("Empate! O jogo terminou sem vencedor.")

jogo_da_velha()
