import requests

url='http://ddragon.leagueoflegends.com/cdn/12.13.1/data/en_US/champion/Aatrox.json'
url2='http://ddragon.leagueoflegends.com/cdn/12.13.1/data/en_US/champion/Ahri.json'
url3='http://ddragon.leagueoflegends.com/cdn/12.13.1/data/en_US/champion/Amumu.json'


res=requests.get(url).json()
res2=requests.get(url2).json()
res3=requests.get(url3).json()

champ_lst=(res['data']['Aatrox']['key'], res['data']['Aatrox']['name'])
champ_lst2=(res['data']['Ahri']['key'], res['data']['Ahri']['name'])
champ_lst3=(res['data']['Ahri']['key'], res['data']['Amumu']['name'])
