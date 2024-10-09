# estrutura de dados set 
# é uma coleção não ordenada de elementos únicos, usamos set para representar conjuntos e eliminar elementos duplicados de outras estruturas de dados

# exemplo

set([1, 2, 1, 5, 6, 1, 5]) # {1, 2, 5, 6}
set('abracadabra') # {'a', 'b', 'c', 'd', 'r'}
set(("palio", "gol", "uno", "palio", "gol")) # {'palio', 'gol', 'uno'}

linguagens = {"Python", "Java", "C", "C++", "Python"}
print(linguagens)
# obs: nem sempre a lista que ele recebe é a mesma que ele retorna ORDENADA, isso acontece porque o set é uma coleção não ordenada

# acessando os dados
# conjuntos não uportam indexação e nem fatiamento, então precisamos iterar sobre eles para acessar os elementos

# union
# retorna a união de dois conjuntos

conjunto_a = {1, 4, 5}
conjunto_b = {4, 5, 6,}

conjunto_a.union(conjunto_b) # {1, 4, 5, 6}

# intersection
# retorna a interseção de dois conjuntos

conjunto_a.intersection(conjunto_b) # {4, 5}

# difference
# retorna a diferença entre dois conjuntos

conjunto_a.difference(conjunto_b) # {1}

# symmetric_difference
# retorna a diferença simétrica entre dois conjuntos

conjunto_a.symmetric_difference(conjunto_b) # {1, 6}

# issubset
# retorna True se um conjunto é subconjunto de outro

conjunto_b.issubset(conjunto_a) # False
conjunto_a.issubset(conjunto_b) # False

# issuperset
# retorna True se um conjunto é superconjunto de outro

conjunto_a.issuperset(conjunto_b) # False
conjunto_b.issuperset(conjunto_a) # False

# isdisjoint
# retorna True se dois conjuntos não têm elementos em comum

conjunto_a.isdisjoint(conjunto_b) # False

# add
# adiciona um elemento ao conjunto

conjunto_a.add(7)

# update
# adiciona vários elementos ao conjunto

conjunto_a.update([8, 9, 10])

# clear
# remove todos os elementos do conjunto

# conjunto_a.clear()

# copy
# retorna uma cópia do conjunto

conjunto_c = conjunto_a.copy()

# discard
# remove um elemento do conjunto, se ele não existir, não faz nada

conjunto_a.discard(7)

# pop
# remove um elemento da frente do conjunto

conjunto_a.pop()

# remove
# remove um elemento do conjunto, se ele não existir, lança um erro

# len
# retorna o tamanho do conjunto

len(conjunto_a)

# in
# verifica se um elemento está presente no conjunto

4 in conjunto_a # True
7 in conjunto_a # False