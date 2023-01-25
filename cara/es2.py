from math import e
from math import pi
class Funzione:
  def eval(self,x): # funzione che restituisce f(x) 
    pass
  def calcola_integrale(self,a,b,M): #funz calcola int
    h = (b - a)/M
    sum = 0
    for i in range(0,M):
      fdix = self.eval(a + i*h)
      sum = sum + fdix
    #list_f = [ eval(self,a + i*h) for i in range(0,M) ] SBAGLIATA
    #integrale = sum(list_f) * h 
    return sum * h

    
class Parabola(Funzione):
  def __init__(self, A,B,C):
    self.A = A
    self.B = B
    self.C = C
  def eval(self,x):
    return (self.A) * x**2 + self.B *x + self.C

    
class Esponenziale(Funzione):
  def __init__(self, d):
    self.d = d
  def eval(self,x):
    return e**(x*self.d)

    
class RazFratta(Funzione):
  def __init__(self, A,B,C,D,E,F):
    self.A = A
    self.B = B
    self.C = C
    self.D = D
    self.E = E
    self.F = F
  def eval(self,x):
    f1 = (self.A) * x**2 + self.B *x + self.C
    f2 = (self.D) * x**2 + self.E *x + self.F
    #try:
      #z = f1/f2
    #except ZeroDivisionError as e:
     # print('la funzione non è definita in quel punto')
    return f1 / f2

funz1= Parabola(1, -2, 0)
print("Primo integrale : {}".format(funz1.calcola_integrale(0,1,500)))

funz2= Esponenziale(2)
print("Secondo integrale : {}".format(funz2.calcola_integrale(- pi/2,pi,500)))

funz3= RazFratta(0, 1, 0,1,0,1)
print("Terzo integrale : {}".format(funz3.calcola_integrale(-2,2,500)))