n = int(input("Digite uma nota entre 0 e 10: "))
while n < 0 or n > 10:
    print("Valores abaixo de 0 ou acima de 10 não são aceitos")
    n = int(input("Digite uma nota entre 0 e 10: "))
