# Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO
from datetime import date
ano = int(input('Digite o ano que quer analisar. Digite 0 para analisar o ano atual:'))
if ano == 0:
    ano = date.today().year
# Acima importei o recurso date da biblioteca datetime e pedi para, caso seja
# digitado 0 o programa retornará a data atual do computador, e mostrará somente o ano.
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é BISSEXTO!'.format(ano))
else:
    print('O ano {} NÃO é BISSEXTO.'.format(ano))

# ano % 4 == 0" diz que todos os anos divisíveis por 4 são bissextos (2008, 2012, 2016, 2020 etc)
# "ano % 100 != 0" diz que todos os anos divisíveis por 100 NÃO são bissextos, criando "falhas" na sequência (retira-se os anos 1700, 1800, 1900, 2000 etc)
# "ano % 400 == 0" preenche as falhas com somente os números divisíveis por 400 (800, 1200, 1600, 2000 etc)
# Então "ano % 4 == 0 and ano % 100 != 0" é um critério, e "ano % 400 == 0" é outro.
