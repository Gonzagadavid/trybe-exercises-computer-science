"""Exercício 2: 
Suponha agora que você está fazendo o processo seletivo para a ReverseCorp, uma empresa que se especializa em produtos e serviços ao contrário. Na sua entrevista, o seu desafio é demonstrar as suas habilidades de inversão com o seguinte problema:
"Faça uma função que recebe uma lista, e retorna-a na ordem reversa."
ReverseCorp Ligue seu cronômetro de novo, e tente desenvolver esta solução, utilizando a iteração. (Se demorar mais que 10 minutos, pare, 
e prossiga com o conteúdo!)"""

# def ReverseCorp(_list, i=1, result=[]):
#   print(i, result)
#   if i == len(_list):
#     return result
#   result.append(_list[len(_list) - i])
#   return ReverseCorp(_list, i + 1, result)


def reverse(_list, i=1, result=[]):
  return result if i == len(_list) else reverse(_list, i + 1, result + [_list[len(_list) - i]])

# print(ReverseCorp([1,2,3,4,5]))



def reverse(_list):
  return _list if len(_list) < 2 else reverse(_list[1:]) + [_list[0]]


print(reverse([1,2,3,4,5]))
#conteudo

# def reverse(list):
#     reversed_list = []
#     for item in list:
#         reversed_list.insert(0, item)
#     return reversed_list

# def reverse2(list):
#   if len(list) < 2:
#       return list
#   else:
#       return reverse(list[1:]) + [list[0]]