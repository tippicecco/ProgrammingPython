class Power:
  def __init__(self, max):
    self.max = max
    self.n = 0


      
  def __iter__(self):
    return self
    
  def __next__(self):
    if self.n > self.max:
      raise StopIteration
    else:
      result = 2**self.n
      self.n += 1
      return result
    
max = None
try:
  max = int(input('Quanti numeri primi vuoi: '))
except ValueError as e:
  print('non hai inserito un numero errore riscontrato: {}'.format(e))
  exit()

if (max < 0):
  raise Exception('valori negativi  non ammessi')
myPot = Power(max)
[print(pot) for pot in myPot]
