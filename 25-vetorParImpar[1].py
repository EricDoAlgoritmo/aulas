vetor = []
vetorPar = []
vetorImpar = []
for x in range(20):
    n = int(input("Número: "))
    vetor.append(n)
    if n % 2 == 0:
        vetorPar.append(n)
    else:
        vetorImpar.append(n)
print("Vetor: ", vetor)
print("Vetor de pares: ", vetorPar)
print("Vetor de impares:", vetorImpar)