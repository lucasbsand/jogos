import random


def play():
    print("Bem vindo ao jogo de advinhação!")
    print("********************************")

    numero_secreto = random.randrange(1, 10000)
    tentativas = 16

    for rodada in range(1, tentativas + 1):
        numero_do_usuário = int(input("Escreva um número entre 1 e 10000: "))
        print("Você digitou ", numero_do_usuário)

        if numero_do_usuário < 1 or numero_do_usuário > 10000:
            print("Você deve digitar um número entre 1 e 10000.")
            continue

        acertou = numero_secreto == numero_do_usuário
        maior = numero_secreto > numero_do_usuário
        menor = numero_secreto < numero_do_usuário

        if acertou:
            print("Você acertou o número!")
            break
        else:
            if maior:
                print("Você errou. O número é maior do que o que você digitou")

            elif menor:
                print("Você errou. O número é menor do que o que você digitou")

        print("Rodada {} de {} tentativas".format(rodada, tentativas))

    print("Fim do jogo.")


if __name__ == "__main__":
    play()
