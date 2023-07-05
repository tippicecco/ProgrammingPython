class ListaConcatenata:
  class Nodo:  #creo una struct come classe
    val = None
    prossimo = None
  def __init__(self):  #creo puntatore è lista, tramite COSTRUTTORE
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

  def inverti(self):
    
    prec = self.testa
    current = self.testa
    current = current.prossimo
    self.testa = self.testa.prossimo
    prec.prossimo = None
    while(self.testa != None):
      self.testa = self.testa.prossimo
      current.prossimo = prec
      prec=current
      current = self.testa
      
    self.testa = prec
  
      
      
        
      
    

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
n = int(input('aggiungi numero a lista: '))
while(n != -1):
  lista_c.aggiungi(n)
  n = int(input('aggiungi numero a lista: '))
current = lista_c.testa
while current.prossimo is not None:
  #print(current.val)
  current = current.prossimo
#print(current.val)

[print(el) for el in lista_c]
lista_c.inverti()
print("LISTA INVERTITA")
[print(el) for el in lista_c]
#print(1/16)

      
  