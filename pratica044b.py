print('{:=^40}'.format(' LOJAS AUGUSTOSO '))
compras = float(input('Preço das compras R$: '))
print('''FORMAS DE PAGAMENTO:
[ 1 ] à vista dinheiro ou cheque (-10%)
[ 2 ] à vista no cartão (-5%)
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão (+20%) ''' )
opcao = int(input('Qual a opção desejada? '))
if opcao == 1:
    valor = compras - (compras * 10/100)
elif opcao == 2:
    valor = compras - (compras * 5/100)
elif opcao == 3:
    parcela = compras / 2
    print(f'Sua compra será parcelada em 2x vezes SEM JUROS de R${parcela:.2f}.')
    valor = compras
elif opcao == 4:
    np = int(input('Quantas parcelas? '))
    valor = compras + (compras * 20/100)
    vp = valor / np
    print(f'Sua compra será parcelada em {np} vezes COM JUROS de R${vp:.2f}. ')
else:
    print('Opção inválida. Tente novamente. ')
print(f'Sua compra de R${compras:.2f} custará {valor:.2f} no final. ')
