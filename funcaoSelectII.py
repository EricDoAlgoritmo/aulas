def soma(n1,n2,n3):
    s = n1 + n2 + n3
    print("A soma dos numeros é = ", s)

def media(n1,n2,n3):
    med = (n1+n2+n3)/3
    print("A media entre os valores é = ", med)

def maior(n1,n2,n3):
    if n1 > n2 and n1 > n3:
        print("O maior é = ", n1)
    elif n2 > n1 and n2 > n3:
        print("O maior é =", n2)
    else:
        print("O maior é =", n3)

def menor(n1,n2,n3):
    if n1 < n2 and n1 < n3:
        print("O menor é = ", n1)
    elif n2 < n1 and n2 < n3:
        print("O menor é =", n2)
    else:
        print("O menor é =", n3)

def opcao(o):
    if o == 1:
        soma(a,b,c)
    elif o == 2:
        media(a,b,c)
    elif o == 3:
        maior(a,b,c)
    elif o == 4:
        menor(a,b,c)

a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
c = int(input('Digite o primeiro número: '))

op = int(input("Qual operação desaja realizar? [1-soma] [2-media] [3-maior] [4-menor]: "))

while op < 1 or op > 4:
    op = int(input("Qual operação desaja realizar? [1-soma] [2-media] [3-maior] [4-menor]: "))

opcao(op)









