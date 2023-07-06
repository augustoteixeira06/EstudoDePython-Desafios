# Elabore um programa que calcule o valor a ser pago por um produto. considerando o seu preço normal e condição de pagamento: - À vista dinheiro/cheque: 10% de desconto - À vista no cartão: 5% de desconto
# Em até 2x no cartão: preço normal - A partir de 3x no cartão: 20% de juros
print('{:=^40}'.format(' LOJONA DO AUGUSTOSO '))
preço = float(input('Valor da compra: R$ '))
print('''FORMAS DE PAGAMENTO
[ 1 ] À vista dinheiro/cheque
[ 2 ] À vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opção = int(input('Qual é a opçào? '))
if opção == 1:
    total = preço - (preço * 10 / 100)
elif opção == 2:
    total = preço - (preço * 5 / 100)
elif opção == 3:
    total = preço
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R$ {:.2f} SEM JUROS '.format(parcela))
elif opção == 4:
    total = preço + (preço * 20 / 100)
    totalparc = int(input('Qual a quantidade de parcelas? '))
    parcela = total / totalparc
    print('Sua compra será parcelada em {}x de R$ {:.2f} COM JUROS'.format(totalparc, parcela))
else:
    total = preço
    print('\033[31m''OPÇÃO INVÁLIDA. TENTE NOVAMENTE!''\033[m')
print('O valor total a ser pago é: R$ {:.2f}'.format(total))
