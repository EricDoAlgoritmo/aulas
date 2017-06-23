x = 0
while x < 5:
    n = int(input("Idade:"))
    if x == 0:
       ma = n
    if n > ma:
       ma = n
    x = x + 1    
print("A maior idade informada foi: ", ma, "anos")