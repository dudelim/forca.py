import random

def mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

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

letras_certas = ["_" for _ in palavra_secreta]

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
        if erros >= 5:
            enforcou = True

    acertou = "_" not in letras_certas
    print(letras_certas)

if acertou:
    mensagem_vencedor()
else:
    mensagem_perdedor(palavra_secreta)

print("Fim do jogo!")
