i = int(input("Quantas idade serão informadas?"))
print()
for x in range(i):
    n = int(input("Idade:"))
    if x == 0:
       ma = n
    if n > ma:
       ma = n
print("A maior idade informada foi: ", ma, "anos")