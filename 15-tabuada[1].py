n = int(input("Selecone um número entre 1 e 10:"))
while n < 1 or n > 10:
    n = int(input("Selecone um número entre 1 e 10:"))
x = 1
print("Tabuada de: %d" % n)
while x <= 10:
     print("%d X %d = %d" %(n,x,n*x))
     x += 1