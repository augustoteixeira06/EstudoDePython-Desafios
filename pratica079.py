# Programa para adicionar números numa lista, sem aceitar repetições e mostrá-los em ordem crescente no final.
valores = list()
while True:
    n = int(input('Digite um número: '))
    if n not in valores:
        valores.append(n)
    else:
        print('O número está duplicado e não será adicionado. ')
    resposta = str(input('Deseja continuar (S/N)? '))
    if resposta not in 'Ss':
        break
valores.sort()
# Sort é o método usado para deixar os números da lista em ordem crescente.
print(f'Você adicionou os números {valores} na lista. ')
