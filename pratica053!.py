# Crie um programa que leia uma frase qualquer e diga se ela é um
# palíndromo, desconsiderando os espaços.
frase = str(input('Digite uma frase: ')).strip().upper()
# strip para eliminar a contagem de espaços entre as letras.
# upper para deixar tudo em maiúsculas.
palavras = frase.split()
# split para separar os elementos da frase em lista.
junto = ''.join(palavras)
# join para juntar os elementos, com uma 'falta' de espaço, no caso.
inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
print(f' O inverso de {junto} é {inverso}')
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo.')

