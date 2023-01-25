from math import sqrt
from math import pi
class Figura():
  def perimetro(self):
    raise NotImplementedError()
  def area(self):
    raise NotImplementedError()

class Triangolo(Figura):
  def __init__(self, a, b, c):
    self.a = a
    self.b = b
    self.c = c

  def determina(self):
    if(self.a == self.b and self.b==self.c):
      print("Triangolo equilatero")
    elif(self.a == self.b or self.b==self.c or self.a==self.c):
      print("Triangolo isoscele")
    else:
      print("Triangolo scaleno")
  def perimetro(self):
    self.p = (self.a + self.b + self.c )/ 2
    return 2*self.p
  def area(self):
    area = sqrt(self.p * (self.p - self.a)* (self.p - self.b) *(self.p - self.c ))
    return area
      

class Rettangolo(Figura):
  def __init__(self, a, b):
    self.a = a
    self.b = b
  def determina(self):
    if self.a == self.b:
      print('Quadrato')
    else:
      print('Rettangolo')
  def perimetro(self):
    return 2*self.a + 2*self.b
    
  def area(self):
    area = self.a * self.b
    return area
    
class Cerchio(Figura):
  def __init__(self, r):
    self.r = r
  def perimetro(self):
    return 2*self.a + 2*self.b
    
  def area(self):
    area = self.a * self.b
    return areapass

tr= Triangolo(5,5,5)
tr.determina()