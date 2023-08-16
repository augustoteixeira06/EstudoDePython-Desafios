numeros = []
while True:
    numeros.append(int(input('Digite um valor: ')))
    resposta = str(input('Deseja continuar (S/N)? '))
    if resposta not in 'Ss':
        break
print(f'Foram digitados {len(numeros)} valores. ')
numeros.sort(reverse=True)
print(f'Em ordem decrescente, os valores são: {numeros}. ')
if 5 in numeros:
    print('O número 5 está na lista. ')
else:
    print('O número 5 não está na lista. ')
