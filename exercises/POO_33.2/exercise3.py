# Exercício 3: Que tal agora relembrarmos o exercício das figuras geométricas? Implemente o diagrama de 
# classes abaixo.

from abc import ABC, abstractmethod
import math

class FiguraGeometrica(ABC):
  
  @abstractmethod
  def area(self):
    raise NotImplementedError
 
  @abstractmethod
  def perimetro(self):
    raise NotImplementedError


class Quadrado(FiguraGeometrica):
  def __init__(self, lado):
    self.lado

  def area(self):
      return 2 * self.lado

  def perimetro(self):
      return 4 * self.lado


class Retangulo(FiguraGeometrica):
  def __init__(self, base, altura):
    self.base = base
    self.altura = altura

  def area(self):
      return self.base * self.altura

  def perimetro(self):
      return (2 * self.base) + (2 * self.altura)

  
class Circulo(FiguraGeometrica):
  def __init__(self, raio):
    self.raio = raio

  def area(self):
      return math.pi * (self.raio ** 2)

  def perimetro(self):
      return 2 * math.pi * self.raio