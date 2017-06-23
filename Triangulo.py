a = int(input("Lado um: "))
b = int(input("Lado dois: "))
c = int(input("Lado três: "))
if a == b &  b == c:
    print("Equilátero")
elif a == b or b == c or a == c:
    print("Isóceles")
else:
    print("Escaleno")

