i = int(input("Quantas idades serão informadas?"))
print()
for x in range(i):
    n = int(input("Idade:"))
    if x == 0:
       ma = n
       me = n
    if n > ma:
       ma = n
    if n < me:
       me = n
print("A maior idade informada foi: ", ma, "anos")
print("A menor idade informada foi: ", me, "anos")
