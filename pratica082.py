numeros = []
par = []
impar = []
while True:
    numeros.append(int(input('Digite um valor: ')))
    resposta = str(input('Deseja continuar (S/N)? '))
    if resposta not in 'Ss':
        break
for i, v in enumerate(numeros):
    if v % 2 == 0:
        par.append(v)
    else:
        impar.append(v)
print(f'Os números digitados foram: {numeros}. ')
print(f'Os pares são: {par}. ')
print(f'Os ímpares são: {impar}. ')
