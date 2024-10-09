# conjunto não ordenado de pares chave: valor, onde as chaves são únicas e imutáveis e para declarar um dicionário utilizamos chaves {} e os pares chave: valor são separados por vírgula

# exemplo

dicionario = {
    'nome': 'João',
    'idade': 25,
    'cidade': 'São Paulo'
}

dicionario = dict(nome='João', idade=25, cidade='São Paulo')

dicionario['telefone'] = "11999999999"

dados = { 'nome': 'João', 'idade': 25, 'cidade': 'São Paulo' }
dados['cidade'] = 'Rio de Janeiro'
dados['nome'] = 'Maria'

# dicionários aninhados
# podemos ter um dicionário dentro de outro dicionário

pessoas = { 
    'pessoa1': { 'nome': 'João', 'idade': 25 },
    'pessoa2': { 'nome': 'Maria', 'idade': 30 }
}

pessoas['pessoa1']['idade']  # 25

# metodos da dict

# copy
# retorna uma cópia do dicionário

dados = { 'nome': 'João', 'idade': 25, 'cidade': 'São Paulo' }  

# fromkeys
# retorna um dicionário com as chaves especificadas e o valor padrão

dicionario = {}.fromkeys(['nome', 'idade', 'cidade'], 'desconhecido')
dict.fromkeys(['nome', 'idade', 'cidade'], 'desconhecido')

# get
# retorna o valor da chave especificada

dados = { 'nome': 'João', 'idade': 25, 'cidade': 'São Paulo' }
dados.get('nome')  # João

# items
# retorna uma lista de tuplas com chave e valor

dados = { 'nome': 'João', 'idade': 25, 'cidade': 'São Paulo' }
dados.items()  # dict_items([('nome', 'João'), ('idade', 25), ('cidade', 'São Paulo')])

# keys
# retorna uma lista com as chaves do dicionário

dados = { 'nome': 'João', 'idade': 25, 'cidade': 'São Paulo' } 