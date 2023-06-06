import urllib.request, json

url = 'https://api.themoviedb.org/3/discover/movie?sort_by=popularity.desc&api_key=760187072f0c695878af293bdd715dd9'


resposta = urllib.request.urlopen(url)

dados = resposta.read()

jsondata = json.loads(dados)

print(jsondata['results'])