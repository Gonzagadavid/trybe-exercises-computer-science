# Exercício 3: Dado um arquivo contendo estudantes e suas respectivas notas, escreva um programa que lê 
# todas essas informações e filtre mantendo somente as pessoas que estão reprovadas, e escreva seus nomes
# em outro arquivo. A nota miníma para aprovação é 6.

# Arquivo:
# Marcos 10
# Felipe 4
# José 6
# Ana 10
# Maria 9
# Miguel 5



# Exemplo saída:
# Felipe
# Miguel

# 🦜 A função split pode ser utilizada para dividir o nome em uma linha. Ex: 
# line.split -> ["Marcos", "10"]

file = open(file='students.txt', mode='r')
aproveds = open(file='aproveds.txt', mode='w')
reproveds = open(file='reproveds.txt', mode='w')

for line in file:
  note = int(line.split(' ')[1])
  aproveds.write(line) if note >= 6 else reproveds.write(line)


file.close()
aproveds.close()
reproveds.close()
