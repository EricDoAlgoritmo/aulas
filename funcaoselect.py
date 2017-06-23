n1 = int(input("Digite o primeiro numero:"))
n2 = int(input("Digite o o segundo numero:"))
n3 = int(input("Digite o terceiro numero: "))
funcao = input("Para soma digite S, para media digite md, para maior numero digite ma, para menor digite me: ")
if funcao == "s":
    soma = n1 + n2 + n3
    print("A soma dos numeros é = ", soma)
elif funcao == "md":
    media = (n1+n2+n3)/3
    print("A media entre os valores é = ", media)
elif funcao == "ma":
    if n1 > n2 and n1 > n3:
        print("O maior é = ", n1)
    elif n2 > n1 and n2 > n3:
        print("O maior é =", n2)
    else:
        print("O maior é =", n3)
elif funcao == "me":
    if n1 < n2 and n1 < n3:
        print("O menor é = ", n1)
    elif n2 < n1 and n2 < n3:
        print("O menor é =", n2)
    else:
        print("O menor é =", n3)
else:
    print("Nenhum valor valido digitado tente novamente mais tarde.")


