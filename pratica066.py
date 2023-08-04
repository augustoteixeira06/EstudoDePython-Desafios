# Programa para ler números inteiros, calcular a soma entre eles e mostrar a quantidade
# de valores digitados. Também deve conter uma condição de parada.
s = c = 0
while True:
    n = int(input('Digite um número (999 para parar): '))
    if n == 999:
        break
    s += n
    c += 1
# A soma e a contagem são realizadas após a condição de parada para não incluir o 999.
print(f'Você digitou {c} valores e a soma deles é {s}. ')
