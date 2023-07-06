sexo = str(input('Informe o seu sexo (M/F): ')).strip().upper()
while sexo not in 'MF':
    sexo = str(input('''Opção inválida. 
Informe o seu sexo corretamente (M/F): ''')).strip().upper()
print(f'Sexo {sexo} registrado com sucesso. ')
