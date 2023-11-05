import random
import json


def play():
    bem_vindo()
    [categoria, palavra_secreta] = carrega_palavra()

    letras_acertadas = conta_letras(palavra_secreta)
    print("\nDica: {}".format(categoria.upper()))
    print(letras_acertadas)

    acertou = False
    enforcou = False
    erros = 0

    while not acertou and not enforcou:
        chute = qual_chute()

        if chute in palavra_secreta:
            letras_corretas(palavra_secreta, chute, letras_acertadas)
        else:
            print("\nA palavra não possui essa letra")
            erros += 1

        acertou = "_" not in letras_acertadas
        enforcou = erros == 6

        print("\nDica: {}".format(categoria.upper()))
        print(letras_acertadas)

    if acertou:
        print("Parabéns, você acertou a palavra!!")
    elif enforcou:
        print("Que pena, você perdeu... a palavra era {}".format(palavra_secreta))


def bem_vindo():
    print("*********************************")
    print("***Bem vindo ao jogo da forca!***")
    print("*********************************")


def carrega_palavra():
    with open("palavras.json", "r") as file:
        arquivo = json.load(file)

    num_categoria = random.randrange(0, len(arquivo))
    categoria = arquivo[num_categoria].keys()
    nome_categoria = ""

    for nome in categoria:
        nome_categoria = nome

    palavras = arquivo[num_categoria][nome_categoria]
    num_palavra = random.randrange(0, len(palavras))
    palavra_secreta = palavras[num_palavra].upper()

    return [nome_categoria, palavra_secreta]


def conta_letras(palavra):
    return ["_" for letra in palavra]


def qual_chute():
    chute = input("Qual a letra? ")
    chute = chute.strip().upper()
    return chute


def letras_corretas(palavra, chute, letras):
    index = 0
    for letra in palavra:
        if chute == letra:
            letras[index] = letra
            print("\nEncontrei a letra {} na posição {}".format(letra, index + 1))
        index += 1


if __name__ == "__main__":
    play()
