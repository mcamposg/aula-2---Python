import requests
from collections import Counter
from contacoisas import contarpalavras

texto = requests.get("https://bit.ly/2Cu73N6").text
palavras = texto.split()

contador_palavras = Counter(palavras)
contador_palavras.most_common(10)

print (contarpalavras(texto))
