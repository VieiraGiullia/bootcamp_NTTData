# Conhecendo metodos uteis da classe string

curso = "pYtHon"

# Deixa a palavra em maiusculo, minusculo e em formato de titulo
print(curso.upper())
print(curso.lower())
print(curso.title())

aluna = "  giullia "

# Remove os espaços em branco no inicio e no final da string
print(aluna.strip())
print(aluna.lstrip())
print(aluna.rstrip())

aula = "introdução"

# junções e centralização
print(curso.center(20, '*'))
print(".".join(curso))
    
# ex de iteração (o que o join faz)
for letra in curso:
    print(letra, end="-")
print()

# Interpolação de variaveis
# interpolar é inserir uma variavel dentro de uma string

horario = 14

# old style (não recomendado) - %
print("Olá %s, a aula de %s do seu curso de %s começa as %d horas" % (aluna.strip(), aula, curso.lower(), horario))

# metodo format 

# declara as variaveis depois da string
print("Olá {}, a aula de {} do seu curso de {} começa as {} horas".format(aluna.strip(), aula, curso.lower(), horario))

# declara as variaveis dentro da string
print("Olá {aluna}, a aula de {aula} do seu curso de {curso} começa as {horario} horas".format(aluna=aluna.strip(), aula=aula, curso=curso.lower(), horario=horario))

# f-string
print(f"Olá {aluna.strip()}, a aula de {aula} do seu curso de {curso.lower()} começa as {horario} horas")

# formatar strings com f-string

PI = 3.14159

print(f"O valor de PI é {PI:.2f}")
print(f"O valor de PI é {PI:.4f}")
print(f"O valor de PI é {PI:10.2f}") # os 10 primeiros caracteres são espaços em branco

# Fatiamento de strings
# é uma tecnica que permite pegar partes de uma string retornando uma substring, informando o inicio (start), o fim (stop) e o passo (step)

aluna2 = "Giovanna Cecilia de Albuquerque"

aluno2[0] # G
aluno2[:9] # Giovanna
aluno2[10:17] # Cecilia
aluna2[10:17:2] # Ccia
aluna2[:] # Giovanna Cecilia de Albuquerque
aluna2[::-2] # ebuqelA ed ailiceC annaivoG

# Strings multilinhas

# triplas
mensagem = f"""
Olá meu nome é {aluna.strip()},
Eu estou aprendendo Python
"""
mensagem2 = f"""
    Olá meu nome é {aluna.strip()},
        Eu estou aprendendo Python
(essa msg tem recuos diferentes)
"""
