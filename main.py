import httpx
import time

class Cotacoes:
    def __init__(self, codigo, nome, cotacao):
        self.codigo = codigo
        self.nome = nome
        self.cotacao = cotacao

print('Executando API. Aguarde...')

# Endpoint da API de cotações
url = 'https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL'

# Faz uma requisição GET para a API
response = httpx.get(url)

# Analisa a resposta da API como um objeto JSON
data = response.json()

# Lista de objetos Cotacoes
cotacoes = []

# Loop pelos dados da API e cria objetos Cotacoes
for codigo, info in data.items():
    nome = info["name"]
    cotacao = info["bid"]
    cotacao_obj = Cotacoes(codigo, nome, cotacao)
    cotacoes.append(cotacao_obj)

# Imprime as cotações
for cotacao in cotacoes:
    print(f"{cotacao.codigo} - {cotacao.nome}: {cotacao.cotacao}")
 
# 60 segunos deixa aplicação parada    
time.sleep(60)