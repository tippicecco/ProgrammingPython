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

  def evaluate(self,data, fin):
    #---FUNZIONE FIT ---
    #fin = -5
    prev_value = data[0]
      #print(prev_value)
    sum = 0
    for item in data[0:fin]:
        differenza = item - prev_value
        sum = sum + differenza
        prev_value = item
    av_increase = sum / (len(data[:fin]) -1 )

     #CALCOLO ERRORE 
    count = 0
    sum_error = 0
    while (fin != 0) :
      prediction = data[fin -1] + av_increase
      print("predizione : {} dato vero : {}".format(prediction, data[fin]))
      error = abs(data[fin] - prediction)
      sum_error = sum_error + error
      fin = fin + 1
      count = count + 1
      
      
    print(count)
    av_error = sum_error / count
    return av_error



   
    
    

  def fit(self, data):
    #prev_value = None
    fin = -5
    prev_value = data[0]
    #print(prev_value)
    sum = 0
    for item in data[0:fin]:
      differenza = item - prev_value
      sum = sum + differenza
      prev_value = item
    av_increase = sum / (len(data[:fin]) -1 )
    prediction = data[-1] + av_increase
    
    
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
 #print(mod1.avg_global_increment)

print ('VALUTIAMO IL MODELLO')
window = -5 # i dati fino al 60 servono x il training
print ('ABS ACCURACY')
print(mod.evaluate(lista, window))
#expand(lista,mod1)
#print(f"stampo la lista:  {lista}")
#pyplot.plot(lista + [mod1.predict(lista)], color = 'tab:red' )
#pyplot.plot(lista, color = 'tab:blue' )
#pyplot.show()
