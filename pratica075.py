# Programa para guardar valores em uma tupla e mostrá-los no final.
num = (int(input('Digite um núemro: ')),
       int(input('Digite outro núemro: ')),
       int(input('Digite mais um núemro: ')),
       int(input('Digite o último núemro: ')))
print(f'Você digitou {num}')
print(f'O número 9 foi digitado {num.count(9)} vezes')
if 3 in num:
    print(f'O número 3 apareceu na posição {num.index(3)+1}')
else:
    print(f'O valor 3 não foi digitado')
print('Os números pares digitados foram ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')
