import httpx
import time

class Cotacoes:
    def __init__(self, codigo, nome, cotacao):
        self.codigo = codigo
        self.nome = nome
        self.cotacao = cotacao

print('Executando API. Aguarde...')

print('--------------------------')

inicio = time.time()

# Endpoint da API de cotações
url = 'https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL'

# Faz uma requisição GET para a API
response = httpx.get(url)

fim = time.time()

tempo_decorrido = fim - inicio

# Analisa a resposta da API como um objeto JSON
data = response.json()

# Lista de objetos Cotacoes
cotacoes = []

# Loop pelos dados da API e cria objetos Cotacoes
for codigo, info in data.items():
    nome = info["name"]
    cotacao = float(info["bid"])
    cotacao_obj = Cotacoes(codigo, nome, cotacao)
    cotacoes.append(cotacao_obj)

# Imprime as cotações
for cotacao in cotacoes:
    print(f"{cotacao.nome}: {cotacao.cotacao:,.2f}")
    
print('--------------------------')

# determina a unidade de tempo apropriada
if tempo_decorrido < 1:
    unidade = "ms"
    tempo_decorrido *= 1000
elif tempo_decorrido < 60:
    unidade = "s"
else:
    unidade = "min"
    tempo_decorrido /= 60

# formata a saída
if unidade == "ms":
    tempo_decorrido_fmt = f"{tempo_decorrido:.2f} {unidade}"
elif unidade == "s":
    tempo_decorrido_fmt = f"{tempo_decorrido:.2f} {unidade}"
else:
    tempo_decorrido_fmt = f"{tempo_decorrido:.2f} {unidade}"

print("Tempo decorrido:", tempo_decorrido_fmt)

print('--------------------------')

time.sleep(9999)