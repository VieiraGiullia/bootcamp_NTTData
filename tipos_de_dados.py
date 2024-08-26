print(1 + 10)
print(1.5 + 1 + 0.5)
print(True)
print(False)
print("Python")

'''
int() #inteiro
float() #decimais/flutuantes
str() #string
bool() #booleano (T/F)

# tipos built-in

str() #texto
int() , float() , complex() #numéricos
list() , tuple() , range() #sequências
dict() #mapeamento
set() , frozenset() #conjuntos/coleções
bool() #booleano
bytes() , bytearray() , memoryview() #binários
'''

# conversão de tipos
price = 10
print("O preço é " + str(price))

#inteiro para float (decimal)
price = float(price)
print(price)

price = 10/2
print(price)

# conversão por divisão
price = 10
price = (price)

print(price/2)

print(price//2)

# conversão de numerico para string
price = 10.50
age = 20

print("O preço é " + str(price))
print("A idade é " + str(age))
texto = f"O preço é {price} e a idade é {age}" #f-string (formatação de string) - concatenação de variáveis
print(texto) 

# conversão de string para numerico
price = "10.50"
age = "20"

print(float(price))
print(int(age))

# erro de conversão

price = "python"
print(float(price)) #ValueError
