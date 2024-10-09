# Tuplas
# são estruturas de dados imutáveis, ou seja, não podem ser alteradas após a sua criação, podemos criar uma tupla com a função tuple() ou com parênteses

# exemplo
frutas = ('banana', 'maçã', 'uva', 'morango',)
letras = tuple('abacadabra')
numeros = tuple([1, 2, 3, 4, 5])

# acesso direto - igual a listas
frutas[0]  # banana
frutas[-2]  # uva

# Tuplas aninhadas
# podem ter uma tupla dentro de outra tupla

matriz = (
    (1, 2, 'a'),
    (4, 'b', 6),
    ('c', 8, 9)
)

