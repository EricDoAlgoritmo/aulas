n = int(input("Quantidade de alunos:"))
x = 0
acmIMC = 0
acmPeso = 0
acmAltura = 0
while x < n:
    peso = float(input("Peso do %d° aluno:" % (x+1)))
    altura = float(input("Altura do %d° aluno:" % (x+1)))
    imc = peso / (altura * altura)
    print("IMC do %d° aluno: %5.2f" % (x+1,imc))
    acmPeso = acmPeso + peso
    acmAltura = acmAltura + altura
    acmIMC = acmIMC + imc
    x += 1
print(" A média dos pesos é: %5.2f" % (acmPeso/x))
print(" A média das alturas é: %5.2f" % (acmAltura/x))
print(" A média dos IMCs é: %5.2f" % (acmIMC/x))