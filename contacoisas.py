from collections import Counter

def contarpalavras(contavel):
    contador = None
    if type(contavel) == type(str()):
        palavras = contavel.split()

        contador = Counter(palavras)
    else:
        contador = Counter(contavel)

    return contador.most_common(10)
