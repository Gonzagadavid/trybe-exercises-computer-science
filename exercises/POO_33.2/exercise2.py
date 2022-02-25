# Exercício 2: Defina uma classe Estatistica que calcule média, mediana e moda de uma lista de números.

import statistics

# class Estatistica:
#   def __init__(self, lista):
#     self.lista = lista

#   def media(self):
#     return sum(self.lista) / len(self.lista)

#   def mediana(self):
#     sotertedList = sorted(self.lista)
#     middle = self.lista // 2
#     return (sotertedList[middle + 1] + sotertedList[middle - 1]) // 2

class Estatistica:
  def __init__(self, lista):
    self.lista = lista

  def media(self):
    media = statistics.mean(self.lista)
    return f'Média aritmética:{media}'

  def mediana(self):
    mediana = statistics.median(self.lista)
    return f'Média:{mediana}'

  def moda(self):
    moda = statistics.mode(self.lista)
    return f'Média:{moda}'