valor = int(input("Valor a pagar:"))
pago = int(input("Valor pago:"))
print("Troco: ")
troco = pago - valor
cedulas = 0
nota = 50
while True:
    if nota <= troco:
        troco = troco - nota
        cedulas = cedulas + 1
    else:
        if cedulas > 0:
            print("%d cédula(s) de R$%5.2f." % (cedulas,nota))
        if troco == 0:
            break
        elif nota == 50:
            nota = 20
        elif nota == 20:
            nota = 10
        elif nota == 10:
            nota = 5
        elif nota == 5:
            nota = 2
        elif nota == 2:
            nota = 1
        cedulas = 0