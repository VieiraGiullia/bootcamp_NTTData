# estruturas condicionais são utilizadas para tomada de decisões em um programa, ou seja, para decidir se um bloco de instruções será executado ou não

# Exemplo de estrutura condicional simples

idade = 18
habilitacao = True

if idade >= 18 and habilitacao == True:
    print("Você pode dirigir!")
else: 
    print("Você não pode dirigir!")

# Exemplo de estrutura condicional composta

if idade >= 18:
    print("Você pode dirigir!")
elif idade == 17:
    print("Você pode dirigir, mas tem que estar acompanhado de alguém habilitado!")
else:
    print("Você não pode dirigir!")     
    
# outra forma de escrever a estrutura condicional composta

MAIOR_IDADE = 18
IDADE_ACOMPANHADO = 17
MENOR_IDADE = 16

idade = int(input("Digite sua idade: "))

if idade >= MAIOR_IDADE:
    print("Você pode dirigir!")
else:    
    if idade == IDADE_ACOMPANHADO:
        print("Você pode dirigir, mas tem que estar acompanhado de alguém habilitado!")
    else:
        print("Você não pode dirigir!")

# Exemplo de estrutura condicional aninhada
  
conta_normal = True
conta_universitaria = False
saldo = float(input("Digite o saldo da sua conta: "))
valor = float(input("Digite o valor do saque: "))
        
if conta_normal:
    
    if saldo >= valor:
        saldo = saldo - valor
        print("Saque efetuado com sucesso!")
    else:
        print("Saldo insuficiente!")
        
elif conta_universitaria:
    if saldo >= valor:
        saldo = saldo - valor
        print("Saque efetuado com sucesso!")
    else:
        print("Saldo insuficiente!")
else:
    print("sistema não reconhecei seu tipo de conta!, entre em contato com o banco!")
    
# if ternario
# O if ternário é uma forma simplificada de escrever uma estrutura condicional, muito utilizada em linguagens de programação como Python, Java, C# e outras.

# Sintaxe:
# valor_se_verdadeiro if condição else valor_se_falso

saldo = 1000
saque = 500

status = "Saque efetuado com sucesso!" if saldo >= saque else "Saldo insuficiente!"

print(status)