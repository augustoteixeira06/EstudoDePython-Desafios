# Programa para ler uma lista com 5 números digitaods pelo usuário, mostrá-los e identificar o maior e
# o menor valor.
lista = []
maior = menor = 0
for c in range(0, 5):
    lista.append(int(input(f'Digite um número para ser mostrado na posição {c}: ')))
    if c == 0:
        maior = menor = lista[c]
        # Ao identificar o primeiro valor digitado (na posição zero) o programa atribuirá o
        # maior e o menor valor a ele ao mesmo tempo.
    else:
        if lista[c] > maior:
            maior = lista[c]
        if lista[c] < menor:
            menor = lista[c]
    # A partir do segundo valor o programa passará a checar qual o maior e o menor e atribuirá
    # o status ao valor correspondente.
print('='*50)
print(f'Os valores digitados foram {lista} ')
print(f'O maior número é {maior}, localizado nas posições ', end='')
for p, n in enumerate(lista):
    if n == maior:
        print(f'{p}...', end=' ')
print()
print(f'O menor número é {menor}, localizado nas posições ', end='')
for p, n in enumerate(lista):
    if n == menor:
        print(f'{p}...', end=' ')
