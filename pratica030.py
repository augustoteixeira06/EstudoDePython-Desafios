# Crie um programa que leia um número inteiro e mostre se ele é par ou ímpar.
número = int(input('Digite um número:'))
resultado = número % 2
# O resultado será o resto da divisão do número digitado por 2. Qualquer número par dividido por 2 terá o resto igual a 0. Qualquer Ímpar terá o resto igual a 1.
if resultado == 0:
    print('O número {} é PAR!'.format(número))
else:
    print('O número {} é ÍMPAR!'.format(número))
