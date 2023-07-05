class Error(Exception):
  pass
def Frequenziometro(stringa):
  if (type(stringa) is not str):
    raise Error('input non è stringa')
  my_dict = {}
  for item in stringa:
    count = 0
    for item2 in stringa:
      if item == item2:
        count += 1
    if not item in my_dict:
      my_dict[item]=count
  return my_dict

def fatto(x):
  if x == 1:
    return x
  return x * fatto(x-1)

def Permu(dizio):
  lista_val = dizio.values()
  print(lista_val)
  fattor = fatto(sum(lista_val))
  for item in lista_val :
    fattor = fattor / fatto(item)

  return fattor
    
    
  
  
stri= 'ababc'
print(Frequenziometro(stri))
diz =Frequenziometro(stri)

print('le possibili parole sono: ')
print(Permu(diz))
