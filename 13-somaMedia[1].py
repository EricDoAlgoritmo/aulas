x = 0
acm = 0
while x < 5:
    n = float(input("Número: "))
    acm = acm + n
    x = x + 1
media = acm / x
print("A soma dos números digitados = %5.2f" % acm)
print("A média dos números digitados = %5.2f" % media)