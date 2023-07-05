class Error(Exception):
  pass
def sum_list(my_list):
  if len(my_list) == 0:
    return None
  modified_list = []
  for item in my_list:
    if item is None:
      print("Trovato elemento vuoto")
      modified_list.append(0)
    else:
      modified_list.append(item)
  return sum(modified_list)

def mean_list (my_list):
  if len(my_list)== 0:
    return None
  modified_list = []
  for item in my_list:
    if item is None:
      print("Trovato elemento vuoto, assegno 0")
      modified_list.append(0)
    else:
      modified_list.append(item)
  l = 0  
  for it in modified_list:
    if it != 0:
      l = l + 1
  if l== 0: 
    return None
  for i in modified_list:
    print(i)
  return (sum(modified_list))/l  
      


my_list = [6, 7, 8, 6, 5, None]
for item in my_list:
  if item is (str or list):
    raise Error("ci sono elementi non interi o float")
a = sum_list(my_list)
print('a vale: {}'.format(a))
for i, item in enumerate(my_list):
  print('Posizione {}: {}'.format(i, item))

print('media vale: {}'.format(mean_list(my_list)))
