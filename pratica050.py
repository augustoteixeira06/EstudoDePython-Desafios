# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas
# daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
soma = 0
cont = 0
for c in range(1, 7):
    n = int(input('Digite o {}° valor:'.format(c)))
    if n % 2 ==0:
# O programa só vai somar e contar caso o número digitado seja divisível por 2,
# ou seja, par. Se número divido por 2 for igual a 0.
        soma = soma + n
        cont = cont + 1
# Pode ser simplificado como soma += n e cont += 1.
print('Você informou {} números PARES e a soma foi {}'.format(cont, soma))
