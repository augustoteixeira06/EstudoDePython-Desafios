# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar. Calcule o valor da parcela mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.
casa = float(input('Valor da casa: R$'))
salário = float(input('Salário do comprador: R$'))
anos = int(input('Quantidade de anos de financiamento:'))
# Quantidade de anos vezes 12 para saber a quantidade de meses do plano. Dividi-se o valor do bem pelo resultado para calcular o valor da parcela.
prestação = casa / (anos * 12)
mínimo = salário * 30 / 100
print('Para pagar uma casa de R${:.2f} em {} anos'.format(casa, anos), end='')
print(' a prestação será de R${:.2f}'.format(prestação))
if prestação <= mínimo:
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print('Empréstimo NEGADO.')


'''casa = float(input('Qual o valor da casa? R$ '))
salario = float(input('Qual o salário do comprador? R$ '))
anos = int(input('Em quantos anos deseja pagar? '))
prestacao = casa / (anos * 12)
print(f'Para pagar uma casa de R$ {casa:.2f} em {anos} anos a prestação será de R$ {prestacao:.2f}. ')
if prestacao < salario * (30 / 100):
    print('O empréstimo pode ser CONCEDIDO! ')
else:
    print('Empréstimo NEGADO! ')'''
