import csv

def read_csv(filepath):
    table = list()  # Tabela é uma lista de linhas
    with open(filepath) as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            table.append(row)

    return table

titanic_tbl = read_csv("train.csv")

soma_idades = 0
contados = 0
for passg in titanic_tbl:
  try:
    soma_idades += float(passg["Age"])
    contados += 1
  except(ValueError):
    pass

media = soma_idades / contados

print(media)
