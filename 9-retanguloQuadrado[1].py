print("Informe as dimensões do retângulo")
base = int(input("Base: "))
altura = int(input("Altura: "))
print("Área calculada: %dcm²" % (base * altura))
if base == altura:
    print("Área de um quadrado!")