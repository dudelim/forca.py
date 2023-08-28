import random

print("------------------------------")
print("Bem vindo(a) ao jogo da forca!")
print("------------------------------")

arquivo = open("palavras.txt", "r")
palavras = []

for linha in arquivo:
  linha = linha.strip()
  palavras.append(linha)

arquivo.close()

numero = random.randrange(0, len(palavras))
palavra_secreta = palavras[numero].upper()

letras_certas = ["_" for letra in palavra_secreta]

enforcou = False
acertou = False
erros = 0

print(letras_certas)

while not enforcou and not acertou:
    chute = input("Digite uma letra: ").strip().upper()

    if chute in palavra_secreta:
        index = 0
        for letra in palavra_secreta:
            if chute == letra:
                letras_certas[index] = letra
            index += 1
    else:
        erros += 1

    enforcou = erros == 6
    acertou = "_" not in letras_certas
    print(" ".join(letras_certas))

if acertou:
    print("Você ganhou!")
else:
    print("Você perdeu!")
print("Fim do jogo")
