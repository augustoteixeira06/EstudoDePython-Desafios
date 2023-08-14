# Programa para mostrar apenas as vogais das palavras contidas na tupla.
palavras = ('Mesa', 'Cadeira', 'Monitor', 'Gabinete',
            'Headset', 'Teclado', 'Mouse', 'Mousepad',
            'Controle', 'Modem')
for p in palavras:
    print(f'\nA palavra {p} possui as seguintes vogais: ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
