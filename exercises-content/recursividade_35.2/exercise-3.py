"""Exercício 3: Faça um algoritmo recursivo de soma. Esse algoritmo deve receber um número de parâmetro e deve somar todos os números antecessores a ele.
Exemplo:
Número passado por parâmetro à função: 4

Execução: 4 + 3 + 2 + 1

Resultado: 10"""

# def rerc_sum(n, _sum=0):
#   return _sum if not n else rerc_sum(n - 1, _sum + n)

def rerc_sum(n):
  return n and n + rerc_sum(n - 1)


print(rerc_sum(4))


def count_down(n):
  print(n)
  return n and count_down(n - 1)

count_down(5)