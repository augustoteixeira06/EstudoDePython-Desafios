# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados. Ex: Digite um número: 1834 unidade:4 dezena:3 centena:8 milhar:1 
# Método 1: Usando formatação de string:
'''num = int(input('Digite um número entre 0 e 9999:'))
n = str(num)
print('Analisando o número: {}'.format(num))
print('Unidade: {}'.format(n[3]))
print('Dezena: {}'.format(n[2]))
print('Centena: {}'.format(n[1]))
print('Milhar: {}'.format(n[0]))
Dessa forma o programa procura o posicionamento de cada
elemento digitado, partindo de 0. O problema ocorre quando
algo com menos de 4 elementos é digitado.'''
#----------------------------------------------------------
# Método 2: Usando cálculo matemático:
'''u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o número: {}'.format(num))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))'''
# Breve explicação:
# Divisão: 1234 / 10 = 123,4
# Divisão inteira: 1234 //10 = 123
# Módulo: 1234 % 10 = 4
# Pra descobrir a centena se faz isso:
# Faz a divisão inteira por 100: 1234 // 100 = 12
# Depois pega o resultado e dividi por 10, mas pega só o resto dessa divisão (que é o módulo): 12 % 10 = 2
# Ou seja, a centena é 2.


# Código refeito:
from time import sleep
num = int(input('Informe um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f'Analisando o número {num}... ')
sleep(1)
print(f'Unidade: {u} \nDezena {d} \nCentena {c} \nMilhar {m} ')
