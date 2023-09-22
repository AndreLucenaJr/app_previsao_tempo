#todos os importes
import requests
from pprint import pprint

API_key = '1a05332c99683ae41d8eb54519e6d058'

#O usuário escolhe a cidade que quer analisar 
cidade = input('Digite uma cidade: ')

base_url = 'https://api.openweathermap.org/data/2.5/weather?appid='+ API_key + '&q='+ cidade

#tranformando o resposta do base_url em json
dados_tempo = requests.get(base_url).json()

pprint(dados_tempo)
 