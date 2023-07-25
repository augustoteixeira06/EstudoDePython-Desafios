resp = 'S'
soma = cont = maior = menor = 0

while resp in 'Ss':
    # No Python eu posso fazer dessa forma: enquanto resp conter o valor s
    # maiúsculo ou minúsculo.
    n = int(input('Digite um número: '))
    soma += n
    cont += 1
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    resp = str(input('Quer continuar? (S/N)')).upper().strip()
media = soma / cont
print(f'Você digitou {cont} números e a média entre eles é {media:.2f}')
print(f'O maior valor é {maior} e o menor valor é {menor}. ')
