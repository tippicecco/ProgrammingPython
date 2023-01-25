class Primi:
  def __init__(self, lista1,lista2):
    
    self.index = -1
    self.l1 = lista1
    self.l2 = lista2

  def isinside(self):
    #print('controllo indice {}'.format(self.index))
    j = 0
    for j in range(len(self.l2)):
      if (self.l1[self.index] == self.l2[j]):
        return 1
    return 0
      
  def __iter__(self):
    return self
  def __next__(self):
    
    #print('controllo indice {}'.format(self.index))
    if (self.index >= len(self.l1) - 1):
        raise StopIteration
    self.index += 1  
    while self.isinside():
      self.index += 1
      if (self.index >= len(self.l1) - 1):
        raise StopIteration
    p = self.l1[self.index]
    return p

    
    
  
    
l1 = [8,4,7,5,22,11,1,2,3]
l2 = [8,4,7,5,22,11]
myP = Primi(l1,l2)
[print(primo) for primo in myP]
