# menu 

menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

Digite uma opção:
"""

saldo = 0
limite = 500
extrato = ""
num_saque = 0
LIMITE_SAQUE = 3

while True:
    
    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor do déposito: "))
        
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            
        else:
            print("\nA operação falhou, o laor digitado é inválido!")
        
    elif opcao == "2":
        valor = float(input("\nInforme o valor do saque: "))
        
        excede_saldo = valor > saldo
        
        excede_limite = valor > limite
        
        excede_saque = num_saque >= LIMITE_SAQUE
        
        if excede_saldo:
            print("\nA operação falhou! Você não tem salfo suficiente")
        
        elif excede_limite:
            print("\nA operação falhou! O valor do saque excedeu o limite")
            
        elif excede_saque:
            print("\nA operação falhou! O número máximo de saqes foi atingido")
            
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            num_saque += 1
        
        else:
            print("\nA operação falhou! O valor informado é inválido")
            
    elif opcao == "3":
        print("\n*********************** EXTRATO ************************")
        print("\nNão foram realizadas operações " if not extrato else extrato)
        print(f"Saldo: R$ {saldo:.2f}")
        print("*********************************************************")
        
    elif opcao == "4":
        break
    
    else: 
        print("\nOperação inválida, por favor selecione novamente a operação desejada")