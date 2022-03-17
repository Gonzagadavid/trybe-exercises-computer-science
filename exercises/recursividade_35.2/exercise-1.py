
# Exercício 1: Crie um algoritmo não recursivo para contar quantos números pares existem em uma sequência numérica (1 a n).

def pairs(n):
  count = 0
  while n > 0:
    if n % 2 == 0:
      count += 1
    n -= 1
  
  return count


print(pairs(4))
