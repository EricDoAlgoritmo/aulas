vetor = []
x = 0
while x < 10:
    n = float(input("Número: "))
    vetor.append(n)
    x = x + 1
print("Vetor: ", vetor)
x = len(vetor)
print("Números atribuídos na ordem inaversa:")
while x > 0:
    print(vetor[x-1])
    x = x - 1
vetorInverso = []
x = len(vetor)
while x > 0:
    vetorInverso.append(vetor[x-1])
    x = x - 1
print("Vetor com ordem inversa: ", vetorInverso)