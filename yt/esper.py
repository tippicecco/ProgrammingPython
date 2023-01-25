import random
class Person():
  def __init__(self,nome):
    self.nome=nome
  def vincita(nlanci, valore):
    nlanci = 40
    valore = 1
    sum = 0
    for i in  range(nlanci):
      casuale = random.randint(0,1)
      if casuale == 0:
        z = valore
      if casuale == 1:
        z = valore * -1
      sum = sum + z

    print("Il guadagno totale è : {}".format(sum))
    
    
