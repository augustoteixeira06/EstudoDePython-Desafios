# Programa de tabuada com condição de parada.
while True:
    n = int(input('Digite um valor para ver sua tabuada: '))
    if n < 0:
        break
    print('-' * 30)
    for c in range(1, 11):
        print(f'{n} x {c} = {n*c}')
    print('-' * 30)
print('PROGRAMA ENCERRADO. VOLTE SEMPRE. ')
