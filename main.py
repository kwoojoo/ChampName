import requests

url='http://ddragon.leagueoflegends.com/cdn/12.13.1/data/en_US/champion/Aatrox.json'
res=requests.get(url).json()

champ_lst=(res['data']['Aatrox']['key'], res['data']['Aatrox']['name'])