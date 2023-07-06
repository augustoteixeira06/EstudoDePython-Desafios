km = float(input('Qual a quantidade de km rodados?'))
dia = int(input('Qual a quantidade de dias rodados?'))
total = (dia * 60) + (km * 0.15)
print('O valor a pagar é: R${:.2f}'.format(total))
