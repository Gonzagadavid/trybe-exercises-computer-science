from abc import ABC, abstractmethod
import gzip
import json
import csv


class SalesReport(ABC):
    def __init__(self, export_file):
        self.export_file = export_file

    def build(self):
        return [{
                'Coluna 1': 'Dado 1',
                'Coluna 2': 'Dado 2',
                'Coluna 3': 'Dado 3'
                },
                {
                'Coluna 1': 'Dado A',
                'Coluna 2': 'Dado B',
                'Coluna 3': 'Dado C'
                }]

    def compress(self):
        binary_content = json.dumps(self.build()).encode('utf-8')

        with gzip.open(self.export_file + '.gz', 'wb') as compressed_file:
            compressed_file.write(binary_content)

    @abstractmethod
    def serialize(self):
        raise NotImplementedError


class SalesReportJSON(SalesReport):
    def serialize(self):
        with open(self.export_file + '.json', 'w') as file:
            json.dump(self.build(), file)

class SalesReportCsv(SalesReport):
  def serialize(self):
    with open(self.export_file, 'w') as file:
      fileReaded = csv.DictReader(file, delimiter=",", quotechar='"')
      return [row for row in fileReaded]

# Repare que adicionamos o comportamento à classe ascendente ! Fazemos isso porque todos os relatórios terão que ser comprimidos. Isso não é um comportamento especializado, é geral! Então faz sentido torná-la parte da interface da classe. E nossa linguagem permite que classes abstratas tenham métodos concretos (ou seja, que fazem coisas de verdade). As classes herdeiras não são obrigadas a re-implementar esses métodos, apenas os abstratos!
# Mas bom! Até aí tudo muito bom. Mas chega, um tempo depois, uma nova demanda! "Nossos relatórios estão fazendo um sucesso incrível e agora precisamos que clientes possam baixá-los, compactados, lógico, e descompactá-los! Mas nossos clientes não tem perfil técnico e não vão saber descompactar um arquivo .gz, então é obrigatório nós compactarmos ele em .zip também!"
# Você poderia pensar que basta, então, mudar o método .compress() para que compacte em .zip ao invés de .gz mas não! O compactamento do gzip é mais eficiente que o zip . Se mudarmos isso, teremos impacto de custos na nossa infraestrutura e não precisamos disso! Precisamos garantir que todos os relatórios sejam compactados em .zip e em .gz .
# Exercício de Fixação
# Invista cinco minutos tentando resolver esse problema! Spoiler: você encontrará problemas! Quais?


from abc import ABC, abstractmethod
import gzip
import json
from zipfile import ZipFile


class ZipCompressor():
    ''' Nossos compressores terão fixado o local de salvamento
    do arquivo, então vamos defini-lo nos construtores'''
    def __init__(self, filepath='./'):
        self.filepath = filepath

    def compress(self, file_name):
        with ZipFile(file_name + '.zip', 'w') as zip_file:
            zip_file.write(file_name)


class GzCompressor():
    def __init__(self, filepath='./'):
        self.filepath = filepath

    def compress(self, file_name):
        with open(file_name, 'rb') as content:
            with gzip.open(file_name + '.gz', 'wb') as gzip_file:
                gzip_file.writelines(content)


class SalesReport(ABC):
    # Nossa classe agora espera *instâncias* de compressor como um parâmetro.
    # Temos um valor padrão para suportar o código que usava as SalesReport
    # sem parâmetros -- não precisa correr pra re-escrever nada ;)
    def __init__(self, export_file, compressor=GzCompressor()):
        self.export_file = export_file
        self.compressor = compressor

    def build(self):
        return [{
                'Coluna 1': 'Dado 1',
                'Coluna 2': 'Dado 2',
                'Coluna 3': 'Dado 3'
                },
                {
                'Coluna 1': 'Dado A',
                'Coluna 2': 'Dado B',
                'Coluna 3': 'Dado C'
                }]

    # Aqui temos um atributo de classe!
    FILE_EXTENSION = ''

    def get_export_file_name(self):
      # Aqui usamos o atributo de classe
      # Vai fazer mais sentido nas classes herdeiras!
      return self.export_file + self.FILE_EXTENSION

    def compress(self):
        self.serialize()
        self.compressor.compress(self.get_export_file_name())

    @abstractmethod
    def serialize(self):
        raise NotImplementedError


class SalesReportJSON(SalesReport):
    # Nós não reimplementamos o get_export_file_name
    # mas como ele usa um atributo de classe pra pegar a extensão
    # só de redefinir o atributo já vamos conseguir mudar o resultado!
    FILE_EXTENSION = '.json'

    def serialize(self):
        with open(self.get_export_file_name(), 'w') as file:
            json.dump(self.build(), file)


class SalesReportCSV(SalesReport):
    # Sua implementação vai aqui
    pass


# Para testar
relatorio_de_compras = SalesReportJSON('meu_relatorio_1')
relatorio_de_vendas = SalesReportJSON('meu_relatorio_2', ZipCompressor())

relatorio_de_compras.compress()
relatorio_de_vendas.compress()