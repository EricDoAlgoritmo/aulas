n2 = 1
n3 = 1
n1 = 0
n = int(input("Digite um valor para a serie de Fibonacci: "))
print(n2)
print(n3)
while n1 < n:
    n1 = n2 + n3
    if n1 < n:
        print(n1)
    n2 = n3
    n3 = n1



