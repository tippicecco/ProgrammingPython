class Primi:
  def __init__(self, n):
    self.num = 0
    self.n = n
    self.x = 1

  def isprime(self):
    m = self.x - 1
    while m > 1:
      if(self.x % m == 0):
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
    self.num += 1
    if self.num > self.n:
      raise StopIteration
    while (not self.isprime()):
      self.x += 1
    
    p = self.x
    self.x += 1 #trovato  pimo lo salvo nella var
    return p
    
volte = None
try:
  volte = int(input('Quanti numeri primi vuoi: '))
except ValueError as e:
  print('non hai inserito un numero errore riscontrato: {}'.format(e))
if (volte < 0 or volte ==0):
  raise Exception('valori negativi o nulli non ammessi')
myP = Primi(volte)
[print(primo) for primo in myP]
