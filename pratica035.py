# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
r1 = float(input('Digite o comprimento da primeira reta:'))
r2 = float(input('Digite o comprimento da segunda reta:'))
r3 = float(input('Digite o comprimento da terceira reta:'))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
# Para formar um triângulo cada reta precisa ter o comprimento menor do que a soma dos outras duas retas.
    print('Com essas medidas é possível SIM formar um triângulo.')
else:
    print('Com essas medidas NÃO é possível formar um triângulo.')
