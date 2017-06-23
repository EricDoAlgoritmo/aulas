inicio = int(input("Primeiro número: "))
fim = int(input("Segundo número: "))
if inicio < fim:
    while inicio <= fim:
       print(inicio)
       inicio = inicio + 1
else:
    while inicio >= fim:
       print(inicio)
       inicio = inicio - 1 