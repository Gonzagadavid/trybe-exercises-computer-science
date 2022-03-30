# Exercício 6
# Escreva uma função que identifique o único número duplicado em uma lista. Retorne o número duplicado em O(n) .
# Exemplos de entrada e saída:

# entrada = [1, 3, 2, 4, 5, 1]
# # saída: 1

def duplicate(_list):
  uniques = set()
  for n in _list:
    if n in uniques:
      return n
    uniques.add(n)

nums = [1, 3, 2, 4, 5, 1]
print(duplicate(nums))


# Exercício 7
# Sua trajetória no curso foi um sucesso e agora você está trabalhando para a Trybe! Em um determinado módulo, os estudantes precisam entregar dois 
# trabalhos para seguir adiante. Cada vez que um dos trabalhos é entregue, o nome da pessoa fica registrado. Precisamos saber como está o andamento da
# entrega das listas. Para isso, você tem acesso aos nomes das pessoas da turma, bem como ao log de quem já entregou qual lista. A partir das listas abaixo, 
# crie quatro funções que respondem às perguntas a seguir.

estudantes = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
lista1_entregues = ['a', 'd', 'g', 'c']
lista2_entregues = ['c', 'a', 'f']

# Quem ainda não entregou a lista1?
print(set(estudantes).difference(set(lista1_entregues)))

# Quem já entregou as duas listas?
print(set(estudantes).intersection(set(lista1_entregues)).intersection(set(lista2_entregues)))

# Quem já entregou qualquer uma das duas listas?
print((set(lista1_entregues)).union(set(lista2_entregues)))


# Quem ainda não entregou nenhuma das listas?
print(set(estudantes).difference(set(lista1_entregues)).difference(set(lista2_entregues)))
