# Funções 
# Funções são blocos de código que podem ser chamados para executar uma tarefa especifica.

nome = "Giovanna"
curso = "Python"

def saudacao():
    print("Olá, seja bem vindo!")

def saudacao2(nome):
    print(f"Olá {nome}, seja bem vindo!")
    
def saudacao3(curso, nome="Giullia"):
    print(f"Olá {nome}, seja bem vindo ao curso de {curso}!")
    
# Retornando valores
# toda função Python retorna None por padrão. Para retornar um valor, usamos a palavra reservada return

def calcular_total(num):
    return sum(num)

def calcular_antes_depois(num):
    antes = num - 1
    depois = num + 1
    return (antes, depois)

calcular_total([1, 30, 5, 7]) # 43
calcular_antes_depois(10) # (9, 11)

# Funções com argumentos nomeados
# podemos passar argumentos nomeados para uma função, o que facilita a leitura do código, da forma chave = valor

def salvar_carro(marca, modelo, ano, placa):
    print(f"Carro salvo com sucesso {marca}/{modelo}/{ano}/{placa}")
    
salvar_carro("Fiat", "Uno", 2010, "ABC-1234")
salvar_carro(marca="Porshe", modelo="Carrera GT", ano=2020, placa="XYZ-5678")
salvar_carro("Honda", "NSX MK1",  ano=1990, placa="QWE-9012",)

# parâmetros especiais
# podemos passar uma quantidade indefinida de argumentos para uma função, usando o *args

# def f(pos1, pos2, /, pos_or_kw, *, kw1, kw2):
#       -----------    ----------     ----------
#   posicional only / posicional ou keyword / keyword only

# positional only
def criar_carro(modelo, ano, placa, /, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)
    
criar_carro("Eclipse", 1989, "QWE-9012", marca="Mitsubishi", motor="2.0", combustivel="Gasolina")

# keyword only
def criar_carro2(*, modelo, ano, placa, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro2(modelo="Civic", ano=2015, placa="ABC-1234", marca="Honda", motor="2.0", combustivel="Flex")

# keyword anf positional only
def criar_carro3(modelo, ano, placa, /, *, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)
    
criar_carro("Commander", 2025, "XYZ-5678", marca="Jeep", motor="3.0", combustivel="Diesel")

# Objetos de primeira classe
# em Python, funções são objetos de primeira classe, o que significa que podemos passar funções como argumentos para outras funções. Assim podemos atribuir funções a variáveis, passá-las como parâmetros e usá-las como valores em estruturas de dados (listas, tuplas, dicionarios)  e usar como valor de retorno para uma função(clouseres)

def somr(a, b):
    return a + b

def exibir_resultado(funcao, a, b):
    resultado = funcao(a, b)
    print(f"O resultado da operação {a} + {b} = {resultado}")
    
exibir_resultado(somr, 10, 20)
