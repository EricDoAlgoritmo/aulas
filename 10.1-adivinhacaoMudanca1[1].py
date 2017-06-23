from random import randint
print("---- Jogo da adivinhação ----")
n = randint(0,10)
while True:
    print("Tente adivinhar o número aleatório entre 0 e 10")
    chute = int(input("Chute: "))
    if chute == n:
        print("Parábens você acertou!")
        break
    elif chute > n:
        print("Chute alto!")
    else:
        print("Chute baixo!")