class CSVFile():
  # Setto il nome del file
  def __init__(self, name):
    self.name = name
    # Provo ad aprirlo e leggere una riga
    self.can_read = True
    try:
      mio_file = open (self.name, 'r')
      mio_file.readline()
    except Exception as e :
      self.can_read = False
      print("Errore in apertura del file: {}".format(e))
    
  def get_data(self):
    if not self.can_read:
      print("Error file non aperto o illeggibile")
      return None
    else:
       # Inizializzo una lista vuota per salvare tutti i dati
    
      lista=[]
      mio_file=open(self.name, 'r')
    for line in mio_file:
      elements = line.split(",")
      elements[-1] = elements[-1].strip()
      if elements[0] != 'Date':
        lista.append(elements)
    mio_file.close()

    return lista
    
      
mio_file = CSVFile(name='shampoo_sales.csv')
print('Nome del file: "{}"'.format(mio_file.name))
print('Dati contenuti nel file: #"{}"'.format(mio_file.get_data()))  
     

csvfile = CSVFile(name='sha.csv')
print('Nome del file: "{}"'.format(csvfile.name))
print('Dati contenuti nel file: #"{}"'.format(csvfile.get_data()))
