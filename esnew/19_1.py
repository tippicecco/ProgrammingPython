class Ser:
  def __init__(self, x, y,sigma):
    self.current = x
    self.y = y
    self.sigma = sigma
  def __iter__(self):
    self.i = 0
    return self
  def __next__(self):
    if self.current >= self.y:
       raise StopIteration
    else:
      if (self.current + self.i*self.sigma > self.y):
        self.current = self.y
      else:
        self.current = self.current + self.i*self.sigma
        self.i += 1
      return self.current 

mys = Ser(3,10,0.9)
[print(s) for s in mys]