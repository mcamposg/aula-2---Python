#Calcula a idade média dos que morreram e dos que sobreviveram
from lercsv import read_csv

soma_idades = 0
contados = 0
soma_idades_vivos = 0
contados_vivos = 0
soma_idades_mortos = 0
contados_mortos = 0

titanic_tbl = read_csv("train.csv")
for passg in titanic_tbl:

    try:

      soma_idades += float(passg["Age"])
      contados += 1
      if (passg["Survived"] == "1"):
        soma_idades_vivos += float(passg["Age"])
        contados_vivos += 1
      else:
        soma_idades_mortos += float(passg["Age"])
        contados_mortos += 1
    except(ValueError):
        pass

media = soma_idades / contados
media_vivos = soma_idades_vivos / contados_vivos
media_mortos = soma_idades_mortos / contados_mortos

print("A media de idade todos e", "%.1f" % media)
print("A media de idade dos vivos e", "%.1f" % media_vivos)
print("A media de idade dos mortos e", "%.1f" % media_mortos)
