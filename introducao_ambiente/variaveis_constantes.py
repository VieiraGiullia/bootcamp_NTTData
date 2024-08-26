# Variaveis são valores que podem ser alterados, já constantes são valores que não podem ser alterados.

# exemplo de variavel

age = 20
name = "João"
print(name, "tem", age, "anos")

age = 30
name = "Maria"
print(name, "tem", age, "anos")

# Python não tem constante!!! Mas podemos usar variaveis em caixa alta para simular uma constante.

# exemplo de constante

ABS_PATH = "/home/user"
DEBUG = True
STATES = ["SP", "RJ", "MG", "ES"]
AMOUNT = 30.2

print(ABS_PATH)

# Lendo variaveis com o input

# função input() - lê uma string do teclado
name = input("Digite seu nome: ")

# funcão print() - exibe uma string na tela
name = "guilherme"
lastname = "silveira"

print(name, lastname)
print(name, lastname, end="...") #end="" - não pula linha
print(name, lastname, sep="-") #sep="-" - separa os valores

# links uteis
# https://docs.python.org/3/library/functions.html#input
# https://docs.python.org/3/library/functions.html#print