# Gerador de progressão aritimética. Refazendo o exercício 51 usando While.
print('Gerador de PA ')
print('-='*10)
primeiro = int(input('Digite o primeiro termo: '))
razão = int(input('Digite a razão da PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print(f'{termo} -> ', end='')
        termo += razão
        cont += 1
    print('PAUSA! ')
    mais = int(input('Quantos termos você quer mortrar a mais? '))
print(f'Progressão finalizada com {total} termos mostrados. ')
