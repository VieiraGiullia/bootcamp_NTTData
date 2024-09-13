# List
## é uma sequencia de elementos, que podem ser de qualquer tipo de objeto
## é uma estrutura de dados mutável, ou seja, pode ser alterada
## podemos criar lista usando o construtor list() ou [], a função range() ou colocando valores separados por vírgula

# exemplos

frutas = ['maçã', 'banana', 'laranja', 'uva', 'melancia']
frutas = [] # não é necessário passar nenhum valor
letras = list('python') # aqui cada letra é um elemento da lista - ['p', 'y', 't', 'h', 'o', 'n']
numeros = list(range(10)) # cria uma lista com os números de 0 a 9
carro = ['Ferrari', 'F8', 4200000, 2020, 2900, 'PE', True]

print('-----------------------------------------------')

# Acesso direto

## a lista é uma sequencia, portanto podemos acessar os elementos através de índices, contando a partir do 0

# exemplos

frutas[0] # 'maçã'
frutas[1] # 'banana'
frutas[-1] # 'melancia' - índice negativo -> acessa o último elemento 
frutas[-3] # 'uva' 

print('-----------------------------------------------')

# Matriz

# exemplo

matriz = [
    [1, 'a', 3],
    ['b', 5, 6],
    [7, 8, 'c']
]

matriz[0] # [1, 'a', 3]
matriz[0][0] # 1
matriz[0][-1] # 3
matriz[-1][-1] # 'c'

print('-----------------------------------------------')

# Fatiamento
## forma de acessar uma parte da lista

# exemplos

lista = ['p', 'y', 't', 'h', 'o', 'n']

lista[2:] # ['t', 'h', 'o', 'n'] - a partir do índice 2
lista[:3] # ['p', 'y', 't'] - até o índice 3
lista[1:4] # ['y', 't', 'h'] - do índice 1 até o 4
lista[0:3:2] # ['p', 't'] - do índice 0 até o 3, pulando de 2 em 2
lista[::] # ['p', 'y', 't', 'h', 'o', 'n'] - todos os elementos
lista[::-1] # ['n', 'o', 'h', 't', 'y', 'p'] - todos os elementos, invertidos

# iterar lista - FOR   

carrosModelo = ['R8', 'F8', 'GTR', 'GT', '911']
for carro1 in carrosModelo:
    print(carro1)

# função inumerete

for i, carro1 in enumerate(carrosModelo):
    print(f'{i}: {carro1}')
    
print('-----------------------------------------------')   
# compreensão de lista
## forma de criar uma lista a partir de outra lista

# exemplo
# filtro 1

numeros = [1, 21, 65, 48, 97, 3, 5]
pares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
    
# filtro 2

pares = [numero for numero in numeros if numero % 2 == 0]
        # retorno | interação | condição

quadradro = [numero ** 2 for numero in numeros]