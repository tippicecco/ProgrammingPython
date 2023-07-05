class Error(Exception):
  pass
def sum_csv(file_name):
  totsales = 0.0
  giorni = []
  try:
    my_file = open(file_name,"r")
    my_file.readline()
  except Exception:
    print("errore nel leggere il file")
  #my_file.readline()
  for line in my_file:

      

      element = line.split(",")

      data_stringa = element[0]
      componenti_data = data_stringa.split("-")
      #data_interi = [int(comp) for comp in componenti_data]
      data_interi = []
      for comp in componenti_data:
        data_interi.append(int(comp))

    
      giorni.append(data_interi)
      try:
        totsales += float(element[1])
      except ValueError as v:
        print("il valore {} non può essere convertito, errore {}".format(element[1],v))
      
  my_file.close()
  for item in giorni:
    
    print(item)
  if giorni[1][1]<giorni[3][1]:
    print("yessa")
    print(giorni[1][1])
    print(type(giorni[1][1]))

  
  return totsales


print("la somma è {}".format(sum_csv("shampoo.csv"))) 