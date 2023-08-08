valor = int(input('Qual valor você quer sacar? R$ '))
nota = 100
totnota = 0
while True:
    if valor >= nota:
        valor = valor - nota
        totnota = totnota + 1
    else:
        if totnota > 0:
            print(f'Total: {totnota} cédulas de R${nota}')
        if nota == 100:
            nota = 50
        elif nota == 50:
            nota = 20
        elif nota == 20:
            nota = 10
        elif nota == 10:
            nota = 5
        elif nota == 5:
            nota = 1
        totnota = 0
        if valor == 0:
            break
