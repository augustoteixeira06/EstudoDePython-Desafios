# Escreva um programa que leia o ano de nascimento de um atleta de natação e mostra sua categoria, de acordo com a idade: - Até 9 anos: MIRIM - Até 14 anos: INFANTIL - Até 19 anos: JÚNIOR - Até 25 anos: SÊNIOR - Acima: MASTER
from datetime import date
anonasc = int(input('Ano de Nascimento: '))
anoatual = date.today().year
idade = anoatual - anonasc
print('O atleta tem {} anos. '.format(idade))
if idade <= 9:
    print('Categoria: MIRIN. ')
elif idade <=14:
    print('Categoria: INFANTIL. ')
elif idade <=19:
    print('Categoria: JÚNIOR')
elif idade <= 25:
    print('Categoria: SÊNIOR')
elif idade >= 25 and idade <70:
    print('Categoria: MASTER')
elif idade >= 70:
    print('Categoria: ESQUELETO MORTO. DEAD. ZUMBI. CORDYCEPUS.')


'''from datetime import date
ano = int(input('Ano de nascimento: '))
data = date.today().year
idade = data - ano
print(f'O atleta tem {idade} anos. ')
if idade <= 9:
    print('Classificação: MIRIM ')
elif 9 < idade <= 14:
    print('Classificação: INFANTIL ')
elif 14 < idade <= 19:
    print('Classificação: JÚNIOR ')
elif 19 < idade <= 25:
    print('Classificação: SÊNIOR ')
else:
    print('Classificação: MASTER ')'''

