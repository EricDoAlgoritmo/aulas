from random import randint
print("---- Jogo da adivinhação ----")
n = randint(0,10)
tentativa = 0
while True:
    print("Tente adivinhar o número aleatório entre 0 e 10")
    chute = int(input("Chute: "))
    if chute == n:
        print("Parábens você acertou!")
        print("O total de tentativas foi: %d" % tentativa)
        break
    elif chute > n:
        print("Chute alto!")
    else:
        print("Chute baixo!")
    tentativa += 1