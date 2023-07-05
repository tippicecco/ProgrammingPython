#from math import e
#from math import pi
class Funzione:
  def __init__(self, N):
    self.n = N
  def eval(self): # funzione che restituisce f(x) 
    pass
  def f_hat(self,a,b): #funz calcola int
    h = (b - a)/self.n
    
    list_f = [ self.eval(a + i*h) for i in range(0,self.n) ] 
    
    return (sum(list_f))/self.n

    
class Parabola(Funzione):
  
  def eval(self,x):
    return  x**2 + 2 *x 

    


funz1= Parabola(3)
print("Val medio : {}".format(funz1.f_hat(0,6)))