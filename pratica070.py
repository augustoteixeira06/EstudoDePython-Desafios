# Programa para ler o nome e o preço de um produto, analisar e mostrar o total da compra,
# quantos produtos custam mais de mil reais, qual o nome do mais barato e quanto custa.
total = maisdemil = cont = valorbarato = 0
barato = ''
while True:
    produto = str(input('Nome do produto: '))
    valor = float(input('Preço: R$ '))
    cont = cont + 1
    total = total + valor
    if valor > 1000:
        maisdemil = maisdemil + 1
    if cont == 1:
        barato = produto
        # Assim que o contador identificar o primeiro produto:
        valorbarato = valor
        # Esse primeiro produto já recebe o status de mais barato
    else:
        if valor < valorbarato:
            valorbarato = valor
            barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print('-' * 40)
print(' FIM DO PROGRAMA ')
print('-' * 40)
print(f'O total da compra foi de: R$ {total:.2f}')
print(f'Temos {maisdemil} produtos custando mais de mil reais')
print(f'O produto mais barato foi {barato}, que custa R$ {valorbarato:.2f}')
