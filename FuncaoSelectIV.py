def lerNumero():
    a=int(input("Digite um número Inteiro: "))
    return(a)

def soma(a,b,c):
    return(a+b+c)

def media(a,b,c):
    return(soma(a,b,c)/3)

def maior(a,b,c):
    if a>b and a>c:
        M=a
    elif b>a and b>c:
        M=b
    elif c>a and c>b:
        M=c
    return (M)

def menor(a,b,c):
    if a<b and a<c:
        M=a
    elif b<a and b<c:
        M=b
    elif c<a and c<b:
        M=c
    return (M)

cont = "s"

while cont == "s":
    n1=lerNumero()
    n2=lerNumero()
    n3=lerNumero()
    op=int(input("Selecione uma das opções =  Soma  [1] -  Maior  [2] -  Menor  [3] -  Media  [4]: "))

    if op==1:
        x=soma(n1,n2,n3)
        print("A soma dos 3 números é: ",x)
    if op==2:
        x=(maior(n1,n2,n3))
        print ("O maior número é: ",x)
    if op==3:
        x=(menor(n1,n2,n3))
        print ("O menor número é: ",x)
    if op==4:
        x=(media(n1,n2,n3))
        print(" A média é",x)

    cont = input("deseja continuar e reniciar os numeros digitados para o calculo? [s/n]")
