# estruturas sem repetição são utilizadas para tomada de decisões em um programa, ou seja, para decidir se um bloco de instruções será executado ou não

# Exemplo de estrutura sem repetição
a = int(input("Digite um número: "))
print(a)

a += 1
print(a)

a += 1
print(a)

# Comando FOR
# O comando FOR é uma estrutura de repetição que permite executar um bloco de instruções um número conhecido de vezes
# O comando FOR é composto por três partes: a variável de controle, o intervalo de valores e o bloco de instruções

frutas = ["maçã", "banana", "cereja"]
for fruta in frutas:
    print(fruta)

# Neste exemplo, o loop for percorre a lista frutas e imprime cada item. A variável fruta é a variável de controle que percorre a lista frutas

for i in range(5):
    print(i)

# Neste exemplo, o loop for percorre o intervalo de valores de 0 a 4 e imprime cada valor.

for letra in "Python":
    print(letra)

# Neste exemplo, o loop for percorre a string "Python" e imprime cada letra.

# Compreendendo range()
# range(start, stop, step): Gera números de start até stop - 1, incrementando de step em cada iteração.

for i in range(2, 10, 2):
    print(i)

# FOR com ELSE
# O comando ELSE é opcional e é executado após o término do loop FOR

for letra in texto: 
    if letra.upper() in "AEIOU":
        print(letra, end=" ")
else:
    print()

# Comando WHILE
# O comando WHILE é uma estrutura de repetição que permite executar um bloco de instruções várias vezes, enquanto uma condição for verdadeira. Faz sentindo usar o comando WHILE quando o número de iterações é desconhecido

opcao = -1

while opcao != 0:
    opcao = int(input("[1] sacar \n[2] extrato \n [0] sair \nDigite a opção desejada: "))
    print(opcao)
    
    if opcao == 1:
        print("Saque de")
    elif opcao == 2:
        print("extrato")
else :
    print("Fim do programa")
    
# Comando BREAK
# O comando BREAK é utilizado para interromper a execução de um loop FOR ou WHILE

while num != 0:
    num = int(input("informe um número: "))
    
    if num == 0:
        break
    print(num)