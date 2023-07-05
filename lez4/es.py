class CSVFile:
  def __init__(self,file_name):
    self.name = file_name
    self.canread = True  
    try:
      self.csvfile = open(file_name,"r")
      self.csvfile.readline()
    except Exception:
      self.canread = False
      print("errore nella lettura")
  def get_data(self):
    listaliste = []
    if self.canread == False:
      return None
    lista = []
    for line in self.csvfile:
      el = line.split(",")
     
      el[1] = el[1].strip()  # Rimuove il carattere di nuova riga dalla stringa
      lista.append((el))
      
    return lista


shampo = CSVFile("shampu.csv")
print(shampo.name)
shampolista = shampo.get_data()
for item in shampolista:
  print(item)
print(shampolista)

shampo1 = CSVFile("shampu.csv")
print(shampo1.name)
shampolista1 = shampo1.get_data()

print(shampolista1)