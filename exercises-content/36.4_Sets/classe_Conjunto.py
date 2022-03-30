# Exercício 1: Inicializando a classe e adicionando elementos
# Crie uma classe chamada Conjunto ;
# Escreva um construtor que defina uma lista do tamanho necessário. Inicialize todos os valores com False , uma vez que ainda não temos valores adicionados;
# Crie um método add(item) que recebe um valor até 1000 e adiciona no conjunto;
# Na main (dentro de: if __name__ == "__main__": ), instancie um objeto do tipo Conjunto e adicione os valores.

# [0, 10, 100, 1000]

# Exercício 2: Imprimir
# Caso tenhamos que imprimir na tela o nosso objeto, o comando print(conjunto) não irá funcionar. O que será impresso é o endereço de memória onde o objeto está guardado, e não é isso que queremos. Para que o comando print funcione, precisamos que a nossa classe tenha um método chamado __str__ e é o que faremos agora:
# Crie um método com a assinatura abaixo:

# def __str__(self):
#     # retorno: uma string que representa o seu objeto
# Exemplos de entrada e saída:
# Copiar
# A = {1, 2, 3}
# # saída: '{1, 2, 3}'

# B = {7, 2, 10}
# # saída: '{2, 7, 10}'

# C = {}
# # saída: '{}'
# A saída não precisa ser ordenada, até mesmo porque um conjunto não leva a ordem em consideração. A saída pode ser em qualquer ordem, mas provavelmente será mais fácil retornar em ordem. Teste seu método imprimindo os objetos que você criou.

# Exercício 3: is_in
# Caso queiramos saber se um elemento faz parte ou não do conjunto usando o operador in precisamos que a nossa classe tenha um método chamado __contains__ e é o que faremos agora:
# Crie um método com a assinatura abaixo:

# def __contains__(self, item):
#     # retorno: True, caso o elemento faça parte. False, caso o elemento não faça parte.
# Exemplos de entrada e saída:

# A = {1, 2, 3}

# # entrada: 1
# # saída: True

# # entrada: 0
# # saída: False
# Exercício 4: União
# União: Todos os elementos que estão em A OU em B
# Crie um método com a assinatura abaixo, que recebe como parâmetro outro objeto da classe Conjunto :

# def union(self, conjuntoB):
#     # retorno: outro objeto Conjunto com união do próprio objeto com o conjuntoB
# Na main , instancie dois objetos do tipo Conjunto . Preencha o primeiro com os valores de 1 a 10 , e o segundo, com valores de 10 a 20 ;
# Imprima na tela a união dos dois conjuntos.
# Exercício 5: Intersecção
# Intersecção: Todos os elementos que estão em A E em B
# Crie um método com a assinatura abaixo, que recebe como parâmetro outro objeto da classe Conjunto :

# def intersection(self, conjuntoB):
#     # retorno: outro objeto Conjunto com intersecção do próprio objeto com o conjuntoB
# Exemplos de entrada e saída:
# Copiar
# A = {1, 2, 3}
# B = {3, 4, 5}
# # saída: {3}

# C = {0, 3, 6, 9}
# B = {12, 15, 18}
# # saída: {}
# Pronto, passados todos os exercícios temos nossa primeira classe Conjunto implementada! Existem outras operações que deveríamos implementar para torná-la completa, mas vamos fazer isso nos exercícios do conteúdo. Agora vamos prosseguir com o conteúdo para vermos a sintaxe de Set .


class Conjunto:
  def __init__(self):
    self.limit = 1001
    self._bucket = [False for i in range(self.limit)]

  def add(self, item):
    if item > self.limit or (not isinstance(item, int)):
      raise TypeError

    self._bucket[item] = True

  def get_atives(self):
    atives = set()
    for index, value  in enumerate(self._bucket):
      if value:
        atives.add(index)
    return atives
  
  def __str__(self):
    atives = self.get_atives()
    return f'{atives}'

  def __contains__(self, item):
    return self._bucket[item]

  def union(self, conjuntoB):
    unionAB = f'{self.get_atives().union(conjuntoB.get_atives())}'
    return unionAB

  def add_list(self, _list):
    for num in _list:
      self.add(num)

  def intersection(self, conjuntoB):
    return self.get_atives().intersection(conjuntoB.get_atives())

if __name__ == "__main__":
  nums = [0, 10, 100, 1000]
  conjunto = Conjunto()
  conjunto.add_list(nums)
  print(conjunto)
  print(conjunto.__contains__(1))
  print(conjunto.__contains__(0))
  conjuntoA = Conjunto()
  conjuntoA.add_list(list(range(1, 10 + 1)))
  conjuntoB = Conjunto()
  conjuntoB.add_list(list(range(10, 20 + 1)))
  print(conjuntoA.union(conjuntoB))
  print(conjuntoA.intersection(conjuntoB))

