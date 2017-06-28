diaNasc = int(input("Dia nascimento: "))
mesNasc = int(input("Mês nascimanto:"))
anoNasc = int(input("Ano nascimento:"))
diaAtual = int(input("Dia atual:"))
mesAtual = int(input("Mês atual:"))
anoAtual = int(input("Ano atual:"))
idade = anoAtual - anoNasc
if mesAtual < mesNasc:
    idade = idade - 1
elif mesAtual == mesNasc:
    if diaAtual < diaNasc:
        idade = idade - 1
if mesAtual < mesNasc:
    faltam = mesNasc - mesAtual
    mesIdade = 12 - faltam
    if diaAtual < diaNasc:
        mesIdade = mesIdade - 1
elif mesAtual > mesNasc:
    mesIdade = mesAtual - mesNasc
    if diaAtual < diaNasc:
        mesIdade = mesIdade - 1
else:
    if diaAtual >= diaNasc:
        mesIdade = 0
    else:
        mesIdade = 11
if diaAtual < diaNasc:
    faltaDia = diaNasc - diaAtual
    if mesAtual == 4 or mesAtual == 6 or mesAtual == 9 or mesAtual == 11:
        idadeDia = 30 - faltaDia + 1
    elif mesAtual == 2:
        if anoAtual % 4 == 0 and anoAtual % 100 != 0 or anoAtual % 400 == 0:
            idadeDia = 29 - faltaDia
        else:
            idadeDia = 28 - faltaDia
    else:
        idadeDia = 31 - faltaDia - 1
elif diaAtual > diaNasc:
    idadeDia = diaAtual - diaNasc
else:
    idadeDia = 0
print("Você tem %d anos, %d meses e %d dias de vida " % (idade, mesIdade, idadeDia))