from random import randint
palavra = ["arroz", "laranja", "abacaxi"]
aleatorio = palavra[randint(0,len(palavra)-1)]
digitadas = []
acertos = []
erros = 0
print("Jogo da forca")
print("Tente a certar a palavra; você tem 6 chances!")
while True:
    segredo = ""
    for letra in aleatorio:
        if letra in acertos:
            segredo += letra
        else:
            segredo += "-"
    print(segredo)
    if segredo == aleatorio:
        print("Você acertou!")
        break
    tentativa = input("Digite uma letra:").lower().strip()
    if tentativa in digitadas:
        print("Você já tentou esta letra!")
        erros += 1
        if erros == 6:
            print("Enforcado!")
            break
        print("Você ainda possui %d chance(s)" % (6 - erros))
        continue
    else:
        digitadas += tentativa
        if tentativa in aleatorio:
            acertos += tentativa
        else:
            erros += 1
            print("Você errou!")
            print("Você ainda possui %d chance(s)" % (6 - erros))
    if erros == 6:
        print("Enforcado!")
        break
