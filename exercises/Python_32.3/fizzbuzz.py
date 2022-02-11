# Exercício 1: Escreva um programa que retorne uma lista com os valores numéricos de 1 a N, 
# mas com as seguintes exceções :
# Números divisíveis por 3 deve aparecer como 'Fizz' ao invés do número;
# Números divisíveis por 5 devem aparecer como 'Buzz' ao invés do número;
# Números divisíveis por 3 e 5 devem aparecer como 'FizzBuzz' ao invés do número';
# Ex: 3 -> [1, 2, "Fizz"] .

def fizzbuzz(n):
  numbers = list(range(1, n + 1))
  result = ['FizzBuzz'  
    if (num % 3 == 0) and (num % 5 == 0) else 'Fizz' 
    if num % 3 == 0 else 'Buzz' 
    if num % 5 == 0 else num 
    for num in numbers
    ]
  return result


print(fizzbuzz(15))