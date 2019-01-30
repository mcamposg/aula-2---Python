import requests
from collections import Counter

texto = requests.get("https://bit.ly/2Cu73N6").text
palavras = texto.split()

contador_palavras = Counter(palavras)
contador_palavras.most_common(10)

def contarpalavras(contavel):
    contador = None
    if type(contavel) == type(str()):
        palavras = contavel.split()

        contador = Counter(palavras)
    else:
        contador = Counter(contavel)

    return contador.most_common(10)


print (contarpalavras(texto))
