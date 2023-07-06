p = float(input('Digite o valor do produto: R$'))
d = float(input('Digite a porcentagem do desconto:'))
vd = p * d/100
vf = p - vd
print(f'O valor com desconto é: R${vf:.2f}')
