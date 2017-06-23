print("---- Jogo da adivinhação ----")
print("-- Jogador 1 --")
while True:
    n = int(input("Digite um número entre 0 e 10: "))
    if n >= 0 and n <= 10:
        break
    elif n < 0:
        print("Valores abaixo de 0 não são permitidos!")
    else:
        print("Valores acima de 10 não são permitidos!")
print("-- Jogador 2 --")
while True:
    print("Tente adivinhar o número digitado pelo Jogador 1")
    chute = int(input("Chute: "))
    if chute == n:
        print("Parábens você acertou!")
        break
    elif chute > n:
        print("Chute alto!")
    else:
        print("Chute baixo!")
        
