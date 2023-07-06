# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou se passou do prazo.
from datetime import date
anoatual = date.today().year
anonasc = int(input('Ano do nascimento: '))
idade = anoatual - anonasc
print('Quem nasceu em {} completa {} anos em {}.'.format(anonasc, idade, anoatual))
if idade == 18:
    print('Você deve se alistar IMEDIATAMENTE!.')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda faltam {} anos para o alistamento.'.format(saldo))
    ano = anoatual + saldo
    print('Seu alistamento será em {}.'.format(ano))
else:
    saldo = idade - 18
    print('Você deveria ter se alistado há {} anos.'.format(saldo))
    ano = anoatual - saldo
    print('Seu alistamento foi em {}.'.format(ano))


'''from datetime import date
ano = int(input('Digite o ano de nascimento: '))
data = date.today().year
idade = data - ano
print(f'Quem nasceu em {ano} tem {idade} anos em {data}. ')
if idade > 18:
    print(f'Você deveria ter se alistado há {idade - 18} anos. ')
    print(f'Seu alistamento foi em {ano + 18}. ')
elif idade < 18:
    print(f'Ainda faltam {18 - idade} para se alistar. ')
    print(f'Seu alistamento será em {ano + 18}. ')
else:
    print('Você tem que se alistar IMEDIATAMENTE! ')'''
