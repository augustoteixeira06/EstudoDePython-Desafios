# Programa para mostrar por extenso um valor entre 0 e 20 digitado pelo usuário.
# Usar tupla.
extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
           'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
           'doze', 'treze', 'quatorze', 'quinze', 'dezesseis',
           'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    valor = int(input('Digite um número de 0 a 20 para ver seu por extenso: '))
    if 0 <= valor <= 20:
        break
print(f'Você digitou o valor {extenso[valor]}. ')
