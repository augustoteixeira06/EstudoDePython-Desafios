nome = str(input('Digite o nome completo:')).strip()
# str.strip serve para retirar da contagem de caracteres todos os espaços digitados antes ou depois na frase.
print('Analisando seu nome...')
print('Seu nome em maiúsculas é: {}'.format(nome.upper()))
print('Seu nome em minúsculas é: {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
separa = (nome.split())
# comando para separar as palavras. [0] para mostrar somente a primeira palavra
print('Seu primeiro nome é {} e tem {} letras.'.format(separa[0], len(separa[0])))
