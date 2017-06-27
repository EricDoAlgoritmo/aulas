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
print("Você tem %d anos" % idade)