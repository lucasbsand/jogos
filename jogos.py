import adivinhacao
import forca


def escolhe_jogo():
    print("Bem vindo ao ambiente de jogos!")

    jogo = int(input("Escolha um jogo: (1) adivinhação (2) forca "))

    if jogo == 1:
        adivinhacao.play()
    elif jogo == 2:
        forca.play()


if __name__ == "__main__":
    escolhe_jogo()
