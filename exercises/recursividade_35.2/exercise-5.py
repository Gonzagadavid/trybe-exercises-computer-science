# Exercício 4: Escreva um algoritmo recursivo para encontrar o máximo divisor comum ( mdc ) de dois inteiros.

def mdc(num1, num2):
   return mdc(num2, num1 % num2) if num2 else num1