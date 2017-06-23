vetor = []
x = 0
while x < 5:
    n = int(input("Número: "))
    vetor.append(n)
    x = x + 1
print("Vetor: ", vetor)
x = 0
print("Números atribuídos:")
while x < 5:
    print(vetor[x])
    x = x + 1