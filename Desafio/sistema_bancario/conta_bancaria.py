# passo a passo para criar o sistema bancário
# define as variáveis

valor = 0
saldo = 0
limite = 500
extrato = []
total_saque = 0
LIMITE_SAQUE = 3 

# define as funções

def deposito():
    global saldo
    global extrato
    valor = float(input("Digite o valor do deposito: "))
    
    if valor > 0:
        saldo += valor
        extrato.append(f"Depósito: R$ {valor:.2f}") 
        print(f"Deposito de R$ {valor} realizado com sucesso")
    else:
        print("Valor inválido")

def saque():
    global saldo
    global extrato
    global total_saque
    if total_saque < LIMITE_SAQUE:
        valor = float(input("Digite o valor do saque: "))
        
        if valor > 0 and saldo >= valor and valor <= limite:
            saldo -= valor
            total_saque += 1
            extrato.append(f"Saque: R$ {valor:.2f}")
            print(f"Saque de R$ {valor} realizado com sucesso")
        else:
            print("Valor inválido")
    else:
        print("Limite de saque diário atingido")

def exibir_extrato():
    global extrato
    if len(extrato) == 0:
        print("Não foram realizadas movimentações.")
    else:
        print("Extrato:")
        for operacao in extrato:
            print(operacao)
    print(f"Saldo atual: R$ {saldo:.2f}")

# menu de opções
  
menu = """
Olá, seja bem vindo ao Banco Vieira da Cunha

escolha uma opção para realizar a operação:
[1] - Deposito
[2] - Saque
[3] - Extrato
[4] - Sair
"""
# execução do sistema

while True:
    opcao = input(menu)
    
    if opcao == "1":
        deposito()
    elif opcao == "2":
        saque()
    elif opcao == "3":
        exibir_extrato()
    elif opcao == "4":
        print("Obrigado por usar o Banco Vieira da Cunha, feito para você!")
        break
    else:
        print("Opção inválida")
         
# 1 teste - deu erro pois nõ conseguiu acessar a variável saldo, pois ela está fora do escopo da função, esqueci de adicionar a palavra reservada global para acessar a variável saldo fora do escopo da função         
# 2 teste - limite de saldo diário ok. limite de saldo ok. ajustar o extrato para que haja uma lista de operações realizadas