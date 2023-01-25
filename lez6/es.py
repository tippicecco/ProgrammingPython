class Error(Exception):
  pass
class CSVFile:

    def __init__(self, name):
        
        # Setto il nome del file
        self.name = name
        if type(self.name) != str:
          raise Error('IL NOME DEL FILE NON E UNA STRINGA')
        
        # Provo ad aprirlo e leggere una riga
        self.can_read = True
        try:
            my_file = open(self.name, 'r')
            my_file.readline()
        except Exception as e:
            self.can_read = False
            print('Errore in apertura del file: "{}"'.format(e))


    def get_data(self, start=None, end=None):
        
        if not self.can_read:
            
            # Se nell'init ho settato can_read a False vuol dire che
            # il file non poteva essere aperto o era illeggibile
            print('Errore, file non aperto o illeggibile')
            
            # Esco dalla funzione tornando "niente".
            return None
        if start is not None and type(start)!=int:
            raise Error('parametro start non valido')
        
        if end is not None and type(end)!=int:
            raise Error('parametro end non valido')

        else:
            # Inizializzo una lista vuota per salvare tutti i dati
    
            # Apro il file
            data=[]
            if end is None:
              
              if start is None:
                start=1
                
              elif start < 1:
                raise Error('parametro in entrata {} minore del minimo ammesso, no problem aggiusto'. format(start))
              
              my_file = open(self.name, 'r')  
              i=1
              for line in my_file: 
                if i>=start:
                    if i==1:
                        elements=[]
                    else:
                        elements = line.split(',')
                        elements[-1]=elements[-1].strip()
                        data.append(elements)
                i=i+1
              my_file.close
              if i<= start:
                raise Error('parametro in entrata {} maggiore delle righe del file'. format(start))
                return None
               
               
            else:   #CADO END DIVERSO NONE
              if start is None:
                start=1
                
              elif start < 1:
                raise Error('parametro in entrata {} minore del minimo ammesso, no problem aggiusto'. format(start))
                start=1


              
              if start > end:
                raise Error('parametro in entrata {} maggiore di output {}'. format(start, end))
                return None
              data=[]
              my_file = open(self.name, 'r')
              i=0   
              for line in my_file:
                if i>= start and i<=end: 
                    elements = line.split(',')
                    elements[-1]=elements[-1].strip()
                    data.append(elements)
                i=i+1
              my_file.close() #chiudo file
              if i<= start:
                raise Error('parametro in entrata {} maggiore delle righe del file'. format(start))
                return None
              if i<end: 
                print('Errore nel parametro  end  "{}", va oltre la fine del file. Ho potuto leggere meno delle righe richieste:'.format(end))
              
            
          
            
        
            
            # Quando ho processato tutte le righe, ritorno i dati
            return data
        



class NumericalCSVFile(CSVFile):
    def get_data(self, *arg, **kwarg):
        
        # Chiamo la get_data del genitore 
        string_data = super().get_data( *arg, **kwarg)
        
        # Preparo lista per contenere i dati ma in formato numerico
        numerical_data = []
        
        # Ciclo su tutte le "righe" corrispondenti al file originale 
        for string_row in string_data:
            
            # Preparo una lista di supporto per salvare la riga
            # in "formato" nuumerico (tranne il primo elemento)
            numerical_row = []
            
            # Ciclo su tutti gli elementi della riga con un
            # enumeratore: cosi' ho gratis l'indice "i" della
            # posizione dell'elemento nella riga.
            for i,element in enumerate(string_row):
                
                if i == 0:
                    # Il primo elemento della riga lo lascio in formato stringa
                    numerical_row.append(element)
                    
                else:
                    # Converto a float tutto gli altri. Ma se fallisco, stampo
                    # l'errore e rompo il ciclo (e poi saltero' la riga).
                    try:
                        numerical_row.append(float(element))
                    except Exception as e:
                        print('Errore in conversione del valore "{}" a numerico: "{}"'.format(element, e))
                        break
                
            # Alla fine aggiungo la riga in formato numerico alla lista
            # "esterna", ma solo se sono riuscito a processare tutti gli
            # elementi. Qui controllo per la lunghezza, ma avrei anche potuto
            # usare una variabile di supporto o fare due break in cascata.
            if len(numerical_row) == len(string_row):
                numerical_data.append(numerical_row)

        return numerical_data
star=15
en=5000000000
#if type(star) == str:
#  float(star)
#if type(en) == str:
#  float(en)
mio_file = CSVFile(name='shas.csv')
print('Nome del file: "{}"'.format(mio_file.name))
print('Dati contenuti nel file: "{}"'.format(mio_file.get_data(star,en)))
print("\n ORA SOTTOCLASSE \n")

mio_file_numerico = NumericalCSVFile(name='shas.csv')
print('Nome del file: "{}"'.format(mio_file_numerico.name))
print('Dati contenuti nel file: "{}"'.format(mio_file_numerico.get_data(star,en)))
