import math

# Exercício 1: Crie uma função que receba dois números e retorne o maior deles.
def max_number(num1, num2):
  return num1 if num1 > num2 else num2

print(max_number(4, 5)) # 5
print(max_number(9, 5)) # 9 

# Exercício 2: Calcule a média aritmética dos valores contidos em uma lista.
def average(numbers):
  return sum(numbers) / len(numbers)

list_numbers = [2, 3, 9, 20]

print(average(list_numbers))

# Exercício 3: Faça um programa que, dado um valor n qualquer, tal que n > 1 , 
# imprima na tela um quadrado feito de asteriscos de lado de tamanho n . Por exemplo:

# n = 5

# *****
# *****
# *****
# *****
# *****
# 🦜 Dica: Pyth
# on sabe multiplicar sequências! Por exemplo, 3 * 'bla' resulta em blablabla . 
# Isso se aplica a listas também, caso você precise.
# Sentiu aí um certo dejavu? 😁

def square(n):
  line = '*' * n
  while n > 0:
    print(line)
    n = n - 1

square(5)


# Exercício 4: Crie uma função que receba uma lista de nomes e retorne o nome com a maior quantidade 
# de caracteres. Por exemplo, para ["José", "Lucas", "Nádia", "Fernanda", "Cairo", "Joana"] , 
# o retorno deve ser "Fernanda" .
# 🦜 Uma dica: Utilize a função len() para verificar o tamanho do nome.
def max_name(names):
  maxx = names[0]
  for name in names:
    if len(name) > len(maxx) :
      maxx = name
  return name

names = ["José", "Lucas", "Nádia", "Fernanda", "Cairo", "Joana"]
print(max_name(names))

# Exercício 5: Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a 
# tinta é vendida em latas de 18 litros, que custam R$ 80,00. Crie uma função que retorne dois valores 
# em uma tupla contendo a quantidade de latas de tinta a serem compradas e o preço total a partir do 
# tamanho de uma parede(em m²).
def print_cost(num):
  tin = math.ceil(num / 3)
  cost = tin * 80
  return (tin, cost)

print(print_cost(20))

# Exercício 6: Crie uma função que receba os três lado de um triângulo e informe qual o tipo de triângulo 
# formado ou "não é triangulo" , caso não seja possível formar um triângulo.
# 🦜 Dica:
#   Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
#   Triângulo Equilátero: três lados iguais;
#   Triângulo Isósceles: quaisquer dois lados iguais;
#   Triângulo Escaleno: três lados diferentes.

def is_triangle(a, b, c):
  if a + b < c or b + c < a or c + a < b:
    return 'não é triangulo'
  if a == b and b == c:
    return 'Triângulo Equilátero'
  if a == b or b == c or c == a:
    return 'Triângulo Isósceles'
  
  return 'Triângulo Escaleno'

print(is_triangle(4, 4, 4))
print(is_triangle(4, 4, 6))
print(is_triangle(4, 5, 7))
print(is_triangle(1, 2, 5))


