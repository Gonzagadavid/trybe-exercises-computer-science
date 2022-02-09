# Conjuntos imutáveis (frozenset)

permissions = frozenset(["member", "group"])  # assim como o set, qualquer estrutura iterável pode ser utilizada para criar um frozenset

permissions.union({"user"})  # novos conjuntos imutáveis podem ser criados à partir do original, mas o mesmo não pode ser modificado

permissions.intersection({"user", "member"})  # retorna um conjunto resultante da intersecção dos conjuntos

permissions.difference({"user"})  # retorna a diferença entre os dois conjuntos

# Dicionários (dict)

people_by_id = {1: "Cássio", 2: "João", 3: "Felipe"}  # elementos no formato "chave: valor" separados por vírgula, envolvidos por chaves

people_by_name = {"Cássio": 1, "João": 2, "Felipe": 3}  # outro exemplo, dessa vez usando strings como chaves (ao contrário de JS, as aspas duplas são obrigatórias)

# elementos são acessados por suas chaves
people_by_id[1]  # saída: Cássio

# elementos podem ser removidos com a palavra chave del
del people_by_id[1]
people_by_id.items()  # dict_items([(1, "Cássio"), (2, "João"), (3, "Felipe")])
# um conjunto é retornado com tuplas contendo chaves e valores

# Utilizando o código abaixo, faça os exercícios de fixação 8, 9 e 10:

info = {
  "personagem": "Margarida",
  "origem": "Pato Donald",
  "nota": "Namorada do personagem principal nos quadrinhos do Pato Donald",
}
# Em JavaScript, não precisávamos colocar a chave do objeto entre aspas, porém, em Python, isso é necessário.

# Exercício 8: O que acontecerá se você tentar acessar o valor da chave "personagem" como fazíamos 
# em JavaScript, utilizando object.key ?
# print(info.personagem)
print(info["personagem"])

# Exercício 9: Insira no objeto uma nova propriedade com o nome de chave "recorrente" e o valor "Sim".
# Em seguida, imprima o objeto no console.
info["recorrente"] = "sim"
print(info)

# Exercício 10: Remova a propriedade cuja chave é "origem" e imprima o objeto no console.
del info["origem"]
print(info)