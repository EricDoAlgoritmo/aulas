def soma(n1,n2,n3):
    total = n1+n2+n3
    return total

def sair():
    print("fim!")

def media(n1,n2,n3):
    resultado = (n1+n2+n3)/3
    return resultado

def maior(n1,n2,n3):
    if n1 == n2 and n2 == n3:
        print("Os valores são iguais!")
        return "none"
    else:
        if n1>n2 and n1>n3:
            ma = n1
        elif n2>n1 and n2>n3:
            ma = n2
        elif n3>n1 and n3>n2:
            ma = n3
        return ma

def menor(n1,n2,n3):
    if n1 == n2 and n2 == n3:
        print("Os valores são iguais!")
        return "none"
    else:
        if n1<n2 and n1<n3:
            me = n1
        elif n2<n1 and n2<n3:
            me = n2
        elif n3<n1 and n3<n2:
            me = n3
        return me

def menu():
    def opcao(o):
        if o == 1:
            resultado = soma(x,y,z)
            print("O resultado da soma é: ", resultado)
        elif o == 2:
            resultado = media(x,y,z)
            print("A media é: ", resultado)
        elif o == 3:
            resultado = maior(x,y,z)
            if resultado != "none":
                print("O maior é: ", resultado)
        elif o == 4:
            resultado = menor(x,y,z)
            if resultado != "none":
                print("O menor é: ", resultado)
        elif o == 5:
            menu()
            return 5
        elif o == 6:
            sair()
            return 6
        return 0
    x = entrada()
    y = entrada()
    z = entrada()
    op = 0
    while op != 6:
        while op != 5 and op != 6:
            print("Qual operação deseja realizar? ")
            print("1-Soma")
            print("2-Média")
            print("3-Maior")
            print("4-Menor")
            print("5-Fornecer novos valores")
            print("6-Sair")
            op = op = opcao(int(input("Selecione uma opção:" )))

def entrada():
    print("Valor: ")
    v = int(input())
    return v

menu()

