class Error(Exception):
  pass
class Model():
  def fit(self,data):
    raise NotImplementedError('Metodo non implementato')
  def predict(self,data):
    raise NotImplementedError('Metodo non implementato')

class IncrementModel(Model):
  def compute_incr(self,data):
    if (type(data) is not list):
      raise TypeError('non è una lista')

    if (data == None):
      raise Error('lista senza valori')
    for item in data:
      
      if(type(item) is int or float):
        print('TEST SUPERATO')
      else:
        raise TypeError('valore non processabile')
  def predict(self, data):
    prev_value = None
    prev_value = data[0]
    #print(prev_value)
    sum = 0
    for item in data:
      differenza = item - prev_value
      sum = sum + differenza
      prev_value = item
    av_increase = sum / (len(data) -1 )
    prediction = data[-1] + av_increase
    return prediction

lista = [ 8,19 ,31,41,50, 'jj', 60.0]
mod = IncrementModel()
#if isinstance(fit() , IncrementModel):
 # print ('vero')
#else:
 #  print ('falso')
mod.compute_incr(lista)
print(mod.predict(lista))