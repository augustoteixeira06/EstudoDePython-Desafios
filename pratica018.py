# Faça um programa que leia um ângulo qualquer e mostre na tela o valor de seno, cosseno e tangente desse ângulo.
import math
an = float(input('Digite um valor do ângulo:'))
sen = math.sin(math.radians(an))
# A função radians serve para converter o valor do ângulo de graus para radianos, que é a medida correta.
print('O SENO de um ângulo de {} é {:.2f}'.format(an, sen))
cos = math.cos(math.radians(an))
print('O COSSENO de um ângulo de {} é {:.2f}'.format(an, cos))
tan = math.tan(math.radians(an))
print('A TANGENTE de um ângulo de {} é {:.2f}'.format(an, tan))
