# Cálculo Juros Simples

# Apresentação
print ('\n\t\t\t -- Cálculo Juros Simples --\n')

# Entrada
C = float (input ('Informe o valor do Capital (C): '))
i = float (input ('Informe o valor da Taxa (i): '))
n = float (input ('Informe o Prazo (n): '))

# Processamento
J = (C * i * n) / 100 # J = Juros

# Saída
print ('O juros é: 'f'{C} * {i} * {n} = R$ {J}')