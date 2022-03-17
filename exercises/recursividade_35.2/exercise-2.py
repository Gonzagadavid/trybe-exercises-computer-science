# Exercício 2: Transforme o algoritmo criado acima em recursivo.

def pairs(n):
  return n and (1 + pairs(n - 1) if n % 2 == 0 else pairs(n -1))
  
  


print(pairs(10))