import requests

url='http://ddragon.leagueoflegends.com/cdn/12.13.1/data/en_US/champion/Aatrox.json'
url2='http://ddragon.leagueoflegends.com/cdn/12.13.1/data/en_US/champion/Ahri.json'

res=requests.get(url).json()
res2=requests.get(url).json()

champ_lst=(res['data']['Aatrox']['key'], res['data']['Aatrox']['name'])
champ_lst2=(res['data']['Ahri']['key'], res['data']['Ahri']['name'])
