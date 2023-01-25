class ListaConcatenata:
  class Nodo:  #creo una struct come classe
    val = None
    prossimo = None
  def __init__(self):  #creo puntatore è listadielementt, tramite COSTRUTTORE
    self.testa = None #puntatore alla testa

  def aggiungi(self,n_val):
    if self.testa is None:
      qnodo = self.Nodo()
      qnodo.val = n_val
      #nodo.prossimo = None no covente
      self.testa = qnodo
    else:
      elemento = self.testa #salvo self testa
      while elemento.prossimo != None :
        elemento = elemento.prossimo
      qnodo = self.Nodo()
      qnodo.val = n_val
      elemento.prossimo = qnodo

  def __iter__(self):
    self.corrente = self.testa
    return self
  def __next__(self):
    if self.corrente is None:
      raise StopIteration
    value = self.corrente.val
    self.corrente = self.corrente.prossimo
    return value


lista_c = ListaConcatenata()
lista_c.aggiungi(5)
lista_c.aggiungi(1)
lista_c.aggiungi(3)
current = lista_c.testa
while current is not None:
  print(current.val)
  current = current.prossimo

[print(el) for el in lista_c]
print(1/16)

      
  