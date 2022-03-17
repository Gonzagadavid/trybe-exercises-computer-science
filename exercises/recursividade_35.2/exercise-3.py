# Exercício 3: Crie um algoritmo recursivo que encontre, em uma lista, o maior número inteiro.

def big_number(_list):
   return len(_list) and (_list[0] if _list[0] > big_number(_list[1:]) else big_number(_list[1:]))
