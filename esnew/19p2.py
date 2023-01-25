class Primi:
  def __init__(self, lista):
    
    self.index = -1
    self.lista = lista

  def isprime(self):
    #print('controllo indice {}'.format(self.index))
    m = self.lista[self.index] - 1
    while m > 1:
      if(self.lista[self.index] % m == 0):
        return 0
      else:
        m = m-1
    if m==1:
      return 1
    if m==0:
      return 1
      
  def __iter__(self):
    return self
  def __next__(self):
    
    #print('controllo indice {}'.format(self.index))
    if (self.index >= len(self.lista) -1 ):
        raise StopIteration
    self.index += 1  
    while not self.isprime():
      self.index += 1
    p = self.lista[self.index]
    return p

    
    
  
    
interi = [8,4,7,5,22,11,15,1,2,3,3]
myP = Primi(interi)
[print(primo) for primo in myP]
