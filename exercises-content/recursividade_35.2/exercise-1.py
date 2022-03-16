""" Exercício 1: Fibonacci: Ligue o cronômetro, e faça a medição de quanto tempo você leva para resolver este problema. Se demorar mais de 10 minutos,
pare! Seu tempo acabou.
começo = [0, 1]
0 + 1 = 1 -> [0, 1, 1]
1 + 1 = 2 -> [0, 1, 1, 2]
1 + 2 = 3 -> [0, 1, 1, 2, 3]
3 + 2 = 5 -> [0, 1, 1, 2, 3, 5]
e assim por diante: 8, 13, 21, 33, 54...
Faça uma função que retorne o enésimo número da sequência de Fibonacci.
"""

def fibonacci(n, seq=[0, 1, 1]):
  if len(seq)- 1 == n:
    return seq[n - 1]

  seq.append(seq[-1] + seq[-2])

  return fibonacci(n, seq)

print(fibonacci(6)) # 5
print(fibonacci(7)) # 8
print(fibonacci(8)) # 13

# 2 minutos


## conteudo

def fibonacci_iter(n):
    sequence = [0, 1]
    if n >= 2:
        for x in range(2, n+1):
            next = sequence[-1] + sequence[-2]
            sequence.append(next)
    return sequence[n]


def fibonacci2(n):
  if n < 2:
      return n
  else:
      return fibonacci(n-1) + fibonacci(n-2)