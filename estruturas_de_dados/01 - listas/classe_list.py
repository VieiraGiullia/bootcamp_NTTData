# métodos da classe list

print('append() - adiciona um elemento ao final da lista')
lista = [] 

lista.append(1) # [1]
lista.append('Python')
lista.append([20, 15, 30])

print(lista) # [1, 'Python', [20, 15, 30]]
print('-----------------------------------------------')    

print('.clear - remove todos os elementos da lista')
lista.clear()

print(lista) # []
print('-----------------------------------------------')

print('.copy() - retorna uma cópia da lista')
lista = [1, 'código', 4, 5]
l2 = lista.copy() 

print(lista) # [1, 'código', 4, 5]

print(id(l2), id(lista)) # 140239366004992 140239366004992)
# ou seja, são listas diferentes

l2[0] = 2
print(l2)
print(lista)
print('-----------------------------------------------')

print('[].count() - retorna o número de vezes que um valor aparece na lista')

cores = ['azul', 'vermelho', 'verde', 'vermelho', 'amarelo', 'vermelho']

cores.count('vermelho') # 3
print('-----------------------------------------------')

print('[].extend() - adiciona elementos de uma lista a outra lista')

linguagens = ['Python', 'Java', 'C++']

print(linguagens) # ['Python', 'Java', 'C++']
linguagens.extend(['JavaScript', 'PHP', 'C++'])
print(linguagens) # ['Python', 'Java', 'C++', 'JavaScript', 'PHP', 'C++']
print('-----------------------------------------------')

print('.index() - retorna o índice do primeiro elemento com o valor especificado')

print(linguagens.index('C++')) # 2
print(linguagens.index('PHP')) # 4

# se você quiser pegar todos os indices, pode usar o count até o index
print('-----------------------------------------------')

print('.pop() - remove o elemento no índice especificado')

linguagens.pop() # remove o último elemento
linguagens.pop(0) # remove o primeiro elemento
print(linguagens) # ['Java', 'C++', 'JavaScript', 'PHP']
print('-----------------------------------------------')

print('.remove() - remove o primeiro item com o valor especificado')

linguagens.remove('C++')
print(linguagens) # ['Java', 'JavaScript', 'PHP']
# se quiser remover todos os elementos com o valor especificado, pode usar um loop ou count
print('-----------------------------------------------')

print('.reverse() - reverte a ordem da lista')
linguagens.reverse()
print(linguagens) # ['PHP', 'JavaScript', 'Java']
print('-----------------------------------------------')

print('.sort() - ordena a lista')
lojas = ['Americanas', 'Magazine Luiza', 'Casas Bahia', 'Submarino', 'Amazon', '']
lojas.sort()

lojas.sort(reverse=True) # ordem reversa
lojas.sort(key=lambda x: len(x)) # ordena pelo tamanho da string
lojas.sort(key=lambda x: len(x), reverse=True) # ordena pelo tamanho da string, em ordem reversa
print('-----------------------------------------------')

print('.len() - retorna o número de elementos da lista')
len(lojas) # 5
print('-----------------------------------------------')   

print('.sorted() - retorna uma lista ordenada')
print(sorted(lojas))
sorted(lojas, key=lambda x: len(x))
sorted(lojas, key=lambda x: len(x), reverse=True) 
