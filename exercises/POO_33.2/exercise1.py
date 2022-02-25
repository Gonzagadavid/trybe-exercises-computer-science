# Exercício 1: Lembra do exercício da TV que já abstraímos? Hoje vamos implementar ele, porém com algumas modificações. Veja o diagrama abaixo:

# Diagrama de classes da TV
# Atributos:
# volume - será inicializado com um valor de 50 e só pode estar entre 0 e 99;
# canal - será inicializado com um valor de 1 e só pode estar entre 1 e 99;
# tamanho - será inicializado com o valor do parâmetro;
# ligada - será inicializado com o valor de False , pois está inicialmente desligado.
# Todos os atributos devem ser privados.
# Métodos:
# aumentar_volume - aumenta o volume de 1 em 1 até o máximo de 99;
# diminuir_volume - diminui o volume de 1 em 1 até o mínimo de 0;
# modificar_canal - altera o canal de acordo com o parâmetro recebido e deve lançar uma exceção ( ValueError ) caso o valor esteja fora dos limites;
# ligar_desligar - alterna o estado da TV entre ligado e desligado ( True / False ).

class Televisao:
  def __init__(self, tamanho ):
    self.volume = 50
    self.canal = 1
    self.tamanho = tamanho
    self.ligada = False

  def aumentar_volume(self):
    if self.volume == 99:
      return 

    self.volume += 1
    print(f'volume: {self.volume}')

  def diminuir_volume(self):
    if self.volume == 1:
      return
  
    self.volume -= 1
    print(f'volume: {self.volume}')
  
  def modificar_canal(self, canalNumber):
    if 1 >  canalNumber > 99:
      raise ValueError('canal não encontrado')

    self.canal = canalNumber
    print(f'canal: {self.canal}')

  def ligar_desligar(self):
    self.ligada = not self.ligada
    
    print('tv ligada' if self.ligada else 'tv desligada')


tv = Televisao(75)
tv.aumentar_volume()
tv.aumentar_volume()
tv.aumentar_volume()
tv.diminuir_volume()
tv.diminuir_volume()
tv.diminuir_volume()
tv.diminuir_volume()
tv.modificar_canal(45)
tv.ligar_desligar()
tv.ligar_desligar()
tv.modificar_canal(101)



