from matplotlib import pyplot
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
      raise Error('non è una lista')

    if (data == None):
      raise Error('lista senza valori')
    for item in data:
      
      if(type(item) is int or float):
        print('TEST SUPERATO')
      else:
        raise Error('valore non processabile')

  def fit(self, data):
    prev_value = None
    prev_value = data[-3]
    #print(prev_value)
    sum = 0
    for item in data[-3:]:
      differenza = item - prev_value
      sum = sum + differenza
      prev_value = item
    av_increase = sum / (len(data[-3:]) -1 )
    prediction = data[-1] + av_increase
    
    increase = prediction - data[-1]
    prev_value = data[0]
    sum = 0
    for item in data[:-3]:
      differenza = item - prev_value
      sum = sum + differenza
      prev_value = item
      
    increase2 = sum / (len(data[:-3]) -1 )
    gl_incr = (increase + increase2 ) / 2
    self.avg_global_increment  = gl_incr
    prediction = gl_incr + data[-1]
    return prediction
    
  def predict(self, data):
    prev_value = None
    prev_value = data[-3]
    #print(prev_value)
    sum = 0
    for item in data[-3:]:
      differenza = item - prev_value
      sum = sum + differenza
      prev_value = item
    av_increase = sum / (len(data[-3:]) -1 )
    prediction = data[-1] + av_increase
    return prediction

    
class FitIncrementModel(IncrementModel):
  #ho tolto il metodo fit qua
    #prev_value = data[0]
    #print(prev_value)
    #sum = 0
    #for item in data:
     # differenza = item - prev_value
      #sum = sum + differenza
      #prev_value = item
    #av_increase = sum / (len(data) -1 )
    #prediction = data[-1] + av_increase
    #self.avg_global_increment = av_increase
    #return prediction

  def predict(self,data):
     #prev_value = data[0]
    #print(prev_value)
    #sum = 0
    #for item in data:
     # differenza = item - prev_value
      #sum = sum + differenza
      #prev_value = item
    #av_increase = sum / (len(data) -1 )
    #prediction = data[-1] + av_increase
    #self.avg_global_increment = av_increase
    #return prediction

    prediction = super().fit(data)
    return prediction
    
    
def expand(data, model):
  print('FACCIO PREDIZ AVANTI')
  data.append(model.predict(data))
  for i in range(0,10):
    print(model.predict(data))
    data.append(int(model.predict(data)))    



    
lista = [8,19,31,41, 50, 52,60, 67, 72, 72,67,72]
#lista = 'cdcd'
print(type(lista))
mod = IncrementModel()
#if isinstance(fit() , IncrementModel):
 # print ('vero')
#else:
 #  print ('falso')
#mod.compute_incr(lista)
print(mod.predict(lista))
print('fittiamo ...')
mod1 = FitIncrementModel()
#mod1.compute_incr(lista)
print(mod1.predict(lista))
print(mod1.fit(lista))
print(mod1.avg_global_increment)

 
#expand(lista,mod1)
print(f"stampo la lista:  {lista}")
pyplot.plot(lista + [mod1.predict(lista)], color = 'tab:red' )
pyplot.plot(lista, color = 'tab:blue' )
pyplot.show()
