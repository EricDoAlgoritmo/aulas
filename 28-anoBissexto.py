bissexto = int(input("Digite um ano:"))
if (bissexto % 4) == 0 and (bissexto % 100) != 0 or (bissexto % 400) == 0:
    print("Bissexto!")
else:
    print("O ano digitado não é bissexto!")
