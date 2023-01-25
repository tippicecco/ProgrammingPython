
class CSVFile:

    def __init__(self, name):
        
        # Setto il nome del file
        self.name = name
        
        
        # Provo ad aprirlo e leggere una riga
        self.can_read = True
        try:
            my_file = open(self.name, 'r')
            my_file.readline()
        except Exception as e:
            self.can_read = False
            print('Errore in apertura del file: "{}"'.format(e))


    def get_data(self):
        
        if not self.can_read:
            
            # Se nell'init ho settato can_read a False vuol dire che
            # il file non poteva essere aperto o era illeggibile
            print('Errore, file non aperto o illeggibile')
            
            # Esco dalla funzione tornando "niente".
            return None

        else:
            # Inizializzo una lista vuota per salvare tutti i dati
            data = []
    
            # Apro il file
            my_file = open(self.name, 'r')

            # Leggo il file linea per linea
            for line in my_file:
                
                # Faccio lo split di ogni linea sulla virgola
                elements = line.split(',')
                
                # Posso anche pulire il carattere di newline 
                # dall'ultimo elemento con la funzione strip():
                elements[-1] = elements[-1].strip()
                
                # p.s. in realta' strip() toglie anche gli spazi
                # bianchi all'inizio e alla fine di una stringa.
    
                # Se NON sto processando l'intestazione...
                if elements[0] != 'Date':
                        
                    # Aggiungo alla lista gli elementi di questa linea
                    data.append(elements)
            
            # Chiudo il file
            my_file.close()
            
            # Quando ho processato tutte le righe, ritorno i dati
            return data



          
class NumericalCSVFile(CSVFile):
  def get_data(self):
    string_data=super().get_data()
    numerical_data = []
    for string_row in string_data:
      numerical_row = [] #LISTA DI SUPPORT
      for i, el in enumerate(string_row): # CICLO FOR OF APPENDING ELEMENTZ
        if i==0:
          numerical_row.append(el)
        else:
          try:
            numerical_row.append(float(el))
          except Exception as e:
            print("ERROR nella conversione di elemento {}, tipo errore {}".format(el,e))
            break

    if len(numerical_row)== len(string_row):
      numerical_data.append(numerical_row)

    return numerical_data
        
      
        
        
    
      
mi_file = NumericalCSVFile(name='sha.csv')
print('Nome del file: "{}"'.format(mi_file.name))


print('Dati  convertiti a float contenuti nel file: "{}"'.format(mi_file.get_data()))
