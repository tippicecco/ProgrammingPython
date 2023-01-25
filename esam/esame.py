class ExamException(Exception):
  pass
class MovingAverage:
  def __init__(self, win):
    self.win = win
    #controlli
    if (type(self.win) is not int):
      raise ExamException('Valore della finestra non è un numero intero')
    if self.win <= 1 :
      raise ExamException('Lunghezza finestra insufficiente,finestra senza significato')
      #fine controlli
    
  def compute(self, lista):
    #controlli
    if (type (lista) is not list):
      raise ExamException('Non è stata inserita una lista')
    if lista == None:
      raise ExamException('Errore,  è stata inserita una lista vuota')
    for item in lista:
      if(type(item) != (int or float) ):
        raise ExamException('il valore {} non è processabile'.format(item))
    if (self.win > len(lista)):
      raise ExamException('lunghezza finestra maggiore di quella della lista')
      
#casi in cui la finestra non suddivide
    z = len(lista)
    accettabile = True
    while accettabile:
      z = z - (self.win - 1)
      if (z== 1):
        accettabile = False
      elif(z<1):
        raise ExamException('finestra non accettabile, alcuni valori lista sono esclusi')
     #-- 

    av_lista = []
    a = 0
    b = self.win
    while b <= len(lista):
      window_list = lista[a:b]
      media = sum(window_list)/self.win
      av_lista.append(media)
      a += self.win -1 
      b += self.win -1

    return av_lista
      
    



awa = [2,4,8,16]
mov_av = MovingAverage(2)
result = mov_av.compute(awa)
print(result)
#from matplotlib import pyplot
#pyplot.plot(result , color = 'tab:red')
#pyplot.plot(awa, color = 'tab:blue')
#pyplot.show()
