# Programa para captar valores digitados pelo usuário e adicioná-los numa lista em ordem crescente, sem
# usar o método 'sort'.
lista = []
for c in range(0, 5):
    n = int(input('Digite um número: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('Adicionado ao final da lista. ')
    else:
        p = 0
        while p < len(lista):
            if n <= lista[p]:
                lista .insert(p, n)
                print(f'Adicionado na posição {p} da lista. ')
                break
            p = p + 1
print(f'Em ordem, os números digitados foram: {lista}')
