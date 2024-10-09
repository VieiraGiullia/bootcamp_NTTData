# introduzindo o módulo datatime
# datatime é um módulo que permite manipular datas e horas em Python

import datetime

d = datetime.date(2024, 10, 8)
print(d)
print(d.today()) # retorna a data atual - 2024-10-08

d_hora = datetime(2024, 10, 8)
print(d_hora)
print(d_hora.today()) # retorna a data e hora atual - 2024-10-08 17:21:00

hora = time(12, 30, 45)
print(hora)
# aware e naive objects - objetos conscientes (info sobre o fuso) e não conscientes (sem info sobre o fuso)

#manipulando datas e horas

tipo_carro = 'P'
tempo_pequeno = 30
tempo_medio = 45
tempo_grande = 60
data_atual = datatime.now() # 2024-10-08 17:21:00
# ou pode usar o .utcnow() para pegar a data e hora atual em UTC

if tipo_carro == 'P':
    data_estimada = data_atual + timedelta(minutes=tempo_pequeno)
    print(f'o carro chegou às {data_atual} e ficará pronto ás {data_estimada}')
elif tipo_carro == 'M':
    data_estimada = data_atual + timedelta(minutes=tempo_medio)
    print(f'o carro chegou às {data_atual} e ficará pronto ás {data_estimada}')
else:
    data_estimada = data_atual + timedelta(minutes=tempo_grande)
    print(f'o carro chegou às {data_atual} e ficará pronto ás {data_estimada}') 

print(d.today() - timedelta(days=1))

resultado = datetime(2023, 7, 25, 10, 19, 20) - timedelta(hours=1)
print(resultado.time())

print(datetime.now().date())

#conversão e formatação de datas e horas

data = datetime.now()
data_string = '08/10/2024'

data = datetime.datetime.strptime(data_string, '%d/%m/%Y')
print(data)

# trabalhando com timezone

import pytz

data = datetime.now(pytz.timezone("Europe/Oslo"))
data2 = datetime.now(pytz.timezone("America/Sao_Paulo"))

print(data)
print(data2)

data_oslo = datetime.now(timezone(timedelta(hours=2)))
data_sao_paulo = datetime.now(timezone(timedelta(hours=-3)))

print(data_oslo)
print(data_sao_paulo)