# 
# Exemplo de como processar dados provenientes de um JSON
#

import urllib.request  
import json

def ManipulaJSON():
    endereco = "https://swapi.dev/api/people/1/"
    webURL = urllib.request.urlopen(endereco)
    if (webURL.getcode() == 200):
        dados = webURL.read()
        oJSON = json.loads(dados)

        print(oJSON)

ManipulaJSON()