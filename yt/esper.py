import random
class Person():
  def __init__(self,nome):
    self.nome=nome
    
  def vincita(self,nlanci, valore):
    
    sum = 0
    for i in  range(nlanci):
      casuale = random.randint(0,1)
      print("controllo casuale {}".format(casuale))
      if casuale == 0:
        z = valore
      if casuale == 1:
        z = valore * -1
      sum = sum + z
    return sum
fra=Person("fra") 
for i in [50]:
  print(fra.vincita(i,10))
    
