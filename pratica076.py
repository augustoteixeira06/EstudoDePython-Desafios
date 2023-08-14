# Programa para mostrar uma listagem de produto e preço formatado numa tabela simples. Usar tupla.
produtos = ('Leite', 3.99,
            'Ovos', 13.99,
            'Pào', 8.99,
            'Manteiga', 9.99,
            'Café', 6.99,
            'Queijo', 7.49,
            'Presunto', 3.59,
            'Brownie', 3.50,
            'Salgado', 3.00,
            'Bolo', 2.50)
print('-'*40)
print(f'{"LISTA DE COMPRAS: CAFÉ DA MANHÃ":^40}')
print('-'*40)
for p in range(0, len(produtos)):
    if p % 2 == 0:
        print(f'{produtos[p]:.<30}', end=' ')
    else:
        print(f'R$ {produtos[p]:.2f}')
