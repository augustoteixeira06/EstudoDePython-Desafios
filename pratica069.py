cont18 = contM = contF20 = 0
while True:
    print('-' * 30)
    print('    CADASTRE UMA PESSOA    ')
    print('-' * 30)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F]')).strip().upper()[0]
    if idade >= 18:
        cont18 = cont18 + 1
    if sexo == 'M':
        contM = contM + 1
    if sexo == 'F' and idade < 20:
        contF20 = contF20 + 1
    resp = ' '
    print('-' * 30)
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Ao todo são {cont18} pessoas maiores de 18 anos ')
print(f'Sendo {contM} homens cadastrados ')
print(f'E {contF20} mulheres com menos de 20 anos ')
