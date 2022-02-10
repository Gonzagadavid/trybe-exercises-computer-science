# Exercício 1: Faça um programa que receba um nome e imprima o mesmo na vertical em escada invertida.
#  Exemplo:

# Entrada:

# PEDRO

# Saída:

# PEDRO
# PEDR
# PED
# PE
# P

name = input('Digite seu nome:')
last = 1
print(name)
while last < len(name):
  print(name[0 : -(last)])
  last = last + 1
