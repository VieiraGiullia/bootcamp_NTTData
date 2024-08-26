# operadores aritmeticos 
# sõa utilizados para realizar operações matemáticas

# adição
print(2 + 2)

#subtração
print(2 - 2)

#multiplicação
print(2 * 2)

#divisão e divisão inteira
print(12 / 3)
print(12 // 2)

#modulo e exponenciação
print(10 % 3)
print(2 ** 3)

# precedência de operadores (é igula a matemática)
print(2 + 3 * 4)
print((2 + 3) * 4)

# Operadores de comparação
# são utilizados para comparar valores e retornar um valor booleano

# igualdade
saldo = 450
saque = 400
print(saldo == saque)

# diferença
print(saldo != saque)

# maior que / maior ou igual
print(saldo > saque)
print(saldo >= saque)

# menor que / menor ou igual
print(saldo < saque)
print(saldo <= saque)

# Operdores de atribuição
# são utilizados para atribuir valores a variáveis ou sobescrever valores

#  atribuição simples
saldo = 450
print(saldo)

# atribuição com soma
saldo += 50
print(saldo)

# atribuição com subtração
saldo -= 100
print(saldo)

# atribuição com multiplicação
saldo *= 2
print(saldo)

# atribuição com divisão
saldo /= 4
print(saldo)

# atribuição com modulo
saldo %= 2
print(saldo)

# atribuição com exponenciação
saldo **= 3
print(saldo)

# Operadores lógicos
# são utilizados para combinar valores booleanos e retornar

saldo = 450
saque = 400
limite = 500

# operador E (and)
print(saldo > saque and saldo < limite)

# operador OU (or)
print(saldo > saque or saldo < limite)

# operador NÃO (not)
print(not saldo > saque)

# Operadores de identidade
# são utilizados para comparar objetos

rua = 'Rua 1'
nome_da_rua = rua

rua is nome_da_rua # ambos apontam para o mesmo objeto
rua is not nome_da_rua # ambos apontam para objetos diferentes