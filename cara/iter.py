class MyNumbers:
# Costruzione dell'iteratore 1, 2, ...
  def __iter__(self):
    self.a = 1 # self.a viene inizializzato ad 1
# iter deve ritornare l'oggetto stesso
    return self
  def __next__(self):
    if self.a == 5:
      raise StopIteration('iterazione fermata')
    x = self.a # copia di self.a in x
    self.a += 1 # incremento self.a di 1
    return x # restituisc

class Series:
  def __init__(self, low, high):
    self.current = low
    self.high = high
  def __iter__(self):
    return self
  def __next__(self):
    if self.current > self.high:
      raise StopIteration
    else:
      self.current += 1
      return self.current - 1

class Universita:
  def __init__(self, lista_studenti, lista_docenti):
    self.lista_studenti = lista_studenti
    self. lista_docenti = lista_docenti
  def __iter__(self):
    self.index = -1 
    return self
  def __next__(self):
    self.index += 1 
    if (self.index == len(self.lista_studenti)):
      raise StopIteration
    return self.lista_studenti[self.index]

myS = Series(1,10)
[print(s) for s in myS]
nlist = Series(1,10)
print(list(nlist))
print('-------')
iterable = list(nlist)
for element in iterable:
  pass
item_obj = iter(iterable)
while True:
  try:
    element = next(item_obj)
    print(element)
  except StopIteration:
    break



print('-------')
myclass = MyNumbers()
myiter = iter(myclass)
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))



mystr = "banana"
myiter1 = iter(mystr)
for item in myiter1:
  print(item)
  print(next(myiter1))
