# Desenvolva um programa que leia o comprimento de três retas, diga ao usuário se elas podem ou não formar um triângulo e depois mostre que tipo de triângulo será formado: -Equilátero: todos os lados iguais -Isósceles: dois lados iguais - Escaleno: todos os lados diferentes
r1 = float(input('Digite o comprimento da primeira reta:'))
r2 = float(input('Digite o comprimento da segunda reta:'))
r3 = float(input('Digite o comprimento da terceira reta:'))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Com essas medidas é possível SIM formar um triângulo ', end='')
    if r1 == r2 == r3:
        print('EQUILÁTERO')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO')
    else:
        print('ISÓSCELES')
else:
    print('Com essas medidas NÃO é possível formar um triângulo. ')

'''s1 = float(input('Primeiro segmento: '))
s2 = float(input('Segundo segmento: '))
s3 = float(input('Terceiro segmento: '))
if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    if s1 == s2 and s1 == s3:
        print('Os segmentos podem formar um triângulo EQUILÁTERO! ')
    elif s1 == s2 and s1 != s3 or s1 == s3 and s1 != s2:
      print('Os segmentos podem formar um triângulo ISÓCELES! ')
    else:
        print('Os segmentos podem formar um triângulo ESCALENO! ')
else:
    print('Os segmentos NÃO PODEM formar um triângulo. ')'''
