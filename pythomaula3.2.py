import csv

with open('products.csv') as arq_cav:
  reader = csv.Dictreader(arq_csv)
  for linha in reader:
      print(linha['ProductName'], linha['QuantityPerUnit'], linha['UnitPrice'])
