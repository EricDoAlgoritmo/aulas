i = int(input("Quantas idades serão informadas?"))
print()
idade = []
for x in range(i):
    n = int(input("Idade:"))
    idade.append(n)
    if x == 0:
       ma = n
       me = n
    if n > ma:
       ma = n
    if n < me:
       me = n
print("A maior idade informada foi: ", ma, "anos")
print("A menor idade informada foi: ", me, "anos")
print("Vetor de idades: ", idade)
