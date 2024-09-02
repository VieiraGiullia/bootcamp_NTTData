# a indentação é uma forma de organizar o código, ela é obrigatória em Python, pois é através dela que o interpretador entende o que é um bloco de código

# Exemplo de indentação
if 5 > 2:
    print("Cinco é maior que dois!") # a função print() está dentro do bloco if, pois está indentada
    
# Exemplo de erro de indentação
'''
if 5 > 2:
print("Cinco é maior que dois!") # a função print() está fora do bloco if, pois não está indentada 
# esta forma de código em JAVA, por exemplo, é válida, pois o bloco de código é delimitado por chaves
'''

# Exemplo de indentação em um bloco de código
if 5 > 2:
    print("Cinco é maior que dois!")
    if 4 > 2:
        print("Quatro é maior que dois!") # a função print() está dentro do bloco if, pois está indentada
    else:
        print("Quatro não é maior que dois!") # a função print() está dentro do bloco else, pois está indentada

        