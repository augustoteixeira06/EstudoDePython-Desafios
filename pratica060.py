n = int(input('Digite um número para calcular sua fatorial: '))
c = n
f = 1
while c > 0:
    print(c, end='')
    print(' x' if c > 1 else ' =', end=' ')
    f *= c
    c -= 1
print(f)