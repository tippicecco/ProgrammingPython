class Fibo:
  def __init__(self, max):
    self.max = max
    self.n = 0
    self.f_0 = 0
    self.f_1 = 1

      
  def __iter__(self):
    return self
  def __next__(self):
    if self.n < self.max: #se sta dentro
      if self.n == 0:
        result = self.f_0
      elif self.n == 1:
        result = self.f_1 
      else:
        result = self.f_0 + self.f_1
        self.f_0 = self.f_1
        self.f_1 = result
        
      self.n += 1
      
      return result

    else:
      raise StopIteration
        
    
max = None
try:
  max = int(input('Quanti numeri  vuoi: '))
except ValueError as e:
  print('non hai inserito un numero errore riscontrato: {}'.format(e))
  exit()

if (max < 0):
  raise Exception('valori negativi  non ammessi')
myPot = Fibo(max)

[print(pot) for pot in myPot]
#iteratore = iter(Fibo(max))
#print('respiro')
#for i in range (max):
# print(next(iteratore))
