import math
class Funzione:
  def eval(self,x):
    pass
  def calcola_integrale(self,a,b,M):
    h = (b - a)/M
    if (a>b):
       #scambio
      tmp = b
      b = a
      a = tmp
    
    #s = 0
    fx = [self.eval(a + i*abs(h)) for i in range(0,M)]
    #una riga senza creare s
    
      #s = s + self.eval(a + i*abs(h))
    #s = s*h
    return sum(fx)*h

class Parabola(Funzione):
  def eval(self,x):
    return x**2 - 2*x 
class Expo(Funzione):
  def eval(self,x):
    return math.e**(2*x) 
class Fratta(Funzione):
  def eval(self,x):
    return x/(x**2 + 1) 

f = Parabola()
print("integrale di parabola è...{} ",format(f.calcola_integrale(0,1,500)))

f1 = Expo()
print("integrale di esponenziale è...{} ",format(f1.calcola_integrale(-math.pi/2,math.pi,500)))

f2 = Fratta()
print("integrale di fratta è...{} ",format(f2.calcola_integrale(-2,2,500)))

print("-------ES LISTE---------")
x = [1,2,3,4,5]
y = [i for i in range(1,6)]
print(y)
if(x==y):
  print("marameooo")