# Exercício 4: Dado o seguinte arquivo no formato JSON , leia seu conteúdo e calcule a porcentagem de 
# livros em cada categoria, em relação ao número total de livros. O resultado deve ser escrito em um 
# arquivo no formato CSV como o exemplo abaixo.
# Saída:
# categoria,porcentagem
# Python,0.23201856148491878
# Java,0.23201856148491878
# PHP,0.23201856148491878
import json
import csv

with open(file = 'amazon.json', mode='r') as file:
  content = file.read()
  list_book = json.loads(content)

  total = 0
  categories = dict()
  for book in list_book:
    for category in book['categories']:
      total += 1
      if category in categories:
        categories[category] += 1
      else: 
        categories[category] = 1

  table_books = []
  for category in categories.keys():
    table_books.append({ 'categoria' :category, 'porcentagem': (categories[category] / total) * 100 })
  
  with open('books.csv', 'w') as f:
    writer = csv.DictWriter(f, fieldnames=['categoria', 'porcentagem'])
    writer.writeheader()
    writer.writerows(table_books)

print(table_books, total)


