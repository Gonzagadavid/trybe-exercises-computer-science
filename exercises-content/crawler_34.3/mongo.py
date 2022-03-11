from pymongo import MongoClient

from pymongo import MongoClient

# Por padrão o host é localhost e porta 27017
# Estes valores podem ser modificados passando uma URI
# client = MongoClient("mongodb://localhost:27017/")
client = MongoClient()
# Em posse da conexão podemos acessar um banco de dados e posteriormente uma coleção:
from pymongo import MongoClient

client = MongoClient()
# o banco de dados catalogue será criado se não existir
db = client.catalogue
# a coleção books será criada se não existir
students = db.books
client.close()  # fecha a conexão com o banco de dados
# Para adicionarmos documentos à nossa coleção utilizamos o método insert_one :
from pymongo import MongoClient

client = MongoClient()
db = client.catalogue
# book representa um dado obtido na raspagem
book = {
    "title": "A Light in the Attic",
}
document_id = db.books.insert_one(book).inserted_id
print(document_id)
client.close()  # fecha a conexão com o banco de dados
# Quando um documento é inserido, um _id único é gerado e retornado.
# Também podemos fazer inserção de múltiplos documentos de uma vez.
from pymongo import MongoClient

client = MongoClient()
db = client.catalogue
documents = [
    {
        "title": "A Light in the Attic",
    },
    {
        "title": "Tipping the Velvet",
    },
    {
        "title": "Soumission",
    },
]
db.books.insert_many(documents)
client.close()  # fecha a conexão com o banco de dados
# Buscas podem ser feitas utilizando os métodos find ou find_one .
from pymongo import MongoClient

client = MongoClient()
db = client.catalogue
# busca um documento da coleção, sem filtros
print(db.books.find_one())
# busca utilizando filtros
for book in db.books.find({"title": {"$regex": "t"}}):
    print(book["title"])
client.close()  # fecha a conexão com o banco de dados
# O nosso cliente é um gerenciador de contexto ( with ), logo podemos utilizá-lo como tal, evitando problemas com o fechamento da conexão com o banco de dados:
from pymongo import MongoClient


with MongoClient() as client:
    db = client.database
    for book in db.books.find({"title": {"$regex": "t"}}):
        print(book["title"])