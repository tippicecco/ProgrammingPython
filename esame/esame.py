class ExamException(Exception):
  pass
class CSVTimeSeriesFile:

    def __init__(self, name):
        
        # Setto il nome del file
        self.name = name
        #ho modificato la classe CSVFile togliendo l'attributo self.can_read
        #poichè il controllo lo faccio direttamente nel metodo get_data

        #impongo che self.name debba essere una stringa, in modo da differenziare il caso in cui il nome non è una stringa ed il caso in cui non c'è un file con quel nome
        if not isinstance(self.name,str):
          raise ExamException('il nome del file non è una stringa')
      

    def get_data(self):
      try:
            #provo ad aprire il file e leggere la prima riga
            my_file = open(self.name, 'r')   
            my_file.readline()               
      except Exception as e:
            #se non riesco stampo il messaggio di errore e ritorno None
            print('Errore in apertura del file: "{}"'.format(e))
            return None
      
    
      # Inizializzo la lista vuota che conterrà la serie storica in forma 
      #di stringa
      string_data = []
    

      # Leggo il file linea per linea
      for line in my_file:
             
        # Faccio lo split di ogni linea sulla virgola
        elements = line.split(',')   
        #Pulisco il carattere di newline            
        elements[-1] = elements[-1].strip() 
        
        # Aggiungo alla lista gli elementi della linea tranne la prima,perchè l'ho saltata con my_file.readline(), perciò se c'è un valore sulla prima riga la funzione get_data non lo inserirà in string_data 
        
        string_data.append(elements)

     
      #creo una lista vuota che conterrà i valori convertiti a intero di 
      #string_data corrispondenti al numero dei passeggeri
      int_data = []
        
      # Ciclo su tutte le "righe" corrispondenti al file originale 
      for string_row in string_data:
        #creo una lista che conterra gli elementi della "riga" che sto # 
        #scorrendo
        int_row = []
        #uso un flag che mi indica se la riga in esame è valida
        riga_valida = True
        
        #Ciclo sugli elementi di una "riga", i ed element mi salvano 
        #l'indice e il valore degli elementi di string_row
        for i,element in enumerate(string_row):
          #faccio il controllo sulla prima "colonna" corrispondente alla 
          #data      
          if i == 0:
            # creo una lista che contiene Anno e Mese della data, che 
            #devono essere separati da '-' 
            date_list = element.split('-')
        
            #se la lista che indica la data non ha lunghezza 2 , cioè è nel 
            #formato Anno Mese ,la riga non è valida
            
            if len(date_list) != 2:  
              print('la data {} non è valida'.format(element))
              riga_valida = False
              break
            #ciclo gli elementi Anno e Mese di date_list
            for value in date_list :
              #se riesco a convertirli ad interi allora i valori sono  
              #corretti altrimenti il flag diventa false
              try :
                value=int(value)
              except Exception:
                riga_valida = False
                print('la data {} non è valida'.format(element))
                break

            # verifico se il mese è valido, compreso tra 1 e 12, 
            # l'istruzione a riga 88 serve per evitare che il programma 
            #provi a convertire a int una stringa che non può essere 
            #convertita
            if riga_valida:    
              if int(date_list[1]) < 1 or int(date_list[1])>12:
                riga_valida = False
                print('la data {} non è valida'.format(element))
                break
              
            
            #tolgo gli evenuali spazi bianchi della data
            element = element.strip()
            # la data la lascio in formato stringa
            int_row.append(element)
            
          #controllo i dati sulla seconda"colonna" corrispondenti al 
          #numero di passeggeri          
          elif i==1:
            
            #tolgo gli spazi bianchi
            element = element.strip()  

            #provo a convertire ad intero i valori corrispondenti al numero 
            #di passeggeri, se ci riesco, inserisco il valore in int_row 
            
            try:   
              int_row.append(int(element))
            #altrimenti catturo l'eccezione ,perciò la riga non è valida, il 
            #flag diventa falso e 
            #stampo il messaggio di errore
            except Exception as e:
              riga_valida= False
              print('Errore in conversione del valore "{}" a intero: "{}"'.format(element, e))  
              
              
        #se il flag riga_valida è vero e string_row contiene più di 1 
        #elemento, aggiungo la lista int_row ad int_data
        if riga_valida and len(string_row)>1:
          int_data.append(int_row)

      
      if int_data == []:
        return None
        
    
      #creo una lista annidata lista_di_date dove ogni elemento è la lista che contiene Anno e Mese interi che mi serve per controllare la presenza di timestamp duplicati oppure fuori ordine
      lista_di_date = []
      #scorro gli elementi di int_data
      for row in int_data:
        date_list = row[0].split('-')
        #creo una lista che mi contiene provvisoriamente la data
        int_date_list=[]
        for value in date_list:
          int_date_list.append(int(value)) 
        lista_di_date.append(int_date_list)
        
      
        
      prev_year=lista_di_date[0][0]
      prev_month = lista_di_date[0][1]
    #Scorro gli elementi di lista_di_date, confrontando l'anno e il mese corrente con quello precedente
      for i,row in enumerate(lista_di_date,1):
        if i>1:
          curr_year = row[0]
          
          curr_month = row[1]

          #Se un anno di una data non è consecutivo oppure lo stesso, la serie non 
          #è ordinata e alzo un'eccezione
          #In realtà questo caso si può verificare anche se per un anno mancano le 
          #misurazioni. Però si assume che ci sia almeno una misurazione per anno

          if curr_year - prev_year > 1 :
            raise ExamException('timestamp fuori ordine')
          if curr_year < prev_year:
            raise ExamException('timestamp fuori ordine')
          if prev_month >= curr_month and prev_year == curr_year:
            if prev_month == curr_month:
              raise ExamException('timestamp duplicato')
            raise ExamException('timestampfuori ordine')

          #Aggiorno prev_year e prev_month
          prev_year = curr_year
          prev_month = curr_month

      #Chiudo il file e ritorno la lista annidata  
      
      my_file.close()     
      return int_data      


def compute_avg_monthly_difference(time_series, first_year, last_year):
  
  #se la lista che contiene la serie storica è vuota alzo un'eccezione
  
  if time_series is None:
    raise ExamException('Errore, la lista è vuota ')

  #Se è presente una sola misurazione nella serie, alzo un eccezione

  if len(time_series) == 1:
    raise ExamException('Errore,la serie storica non è utilizzabile perché contiene una sola misurazione')

  #se first_year e last_year non sono stringhe  i parametri non sono accettati e alzo un eccezione 
  if not isinstance(first_year,str):
    raise ExamException('la variabile first_year deve essere una stringa')
  if not isinstance(last_year,str):
    raise ExamException('la variabile last_year deve essere una stringa')

  #rimuovo gli eventuali spazi bianchi 
  first_year = first_year.strip()
  last_year = last_year.strip()

  #eseguo il controllo sulla correttezza dei parametri, poiché per essere validi devono poter essere convertiti a interi  . Se non riesco a convertirli stampo un messaggio di errore e alzo un eccezione
  try:
    first_year = int(first_year)
  except Exception as e:
    print('Errore nella conversione a intero di first_year ({}),parametro non valido : {}'.format(first_year,e))
    raise

  try:
    last_year = int(last_year)
  except Exception as e:
    print('Errore nella conversione a intero di last_year ({}),parametro non valido : {}'.format(last_year,e))
    raise

  #Se first_year è maggiore di last_year alzo l'eccezione ExamException
  if first_year >= last_year:
    raise ExamException('Errore,last_year deve essere maggiore di first_year ')


  #Creo due variabili che memorizzano l'anno minimo e quello massimo della serie
  first_date_list = time_series[0][0].split('-')
  min_year = int(first_date_list[0])
  
  
  last_date_list = time_series[-1][0].split('-')
  max_year = int(last_date_list[0])

  
  if  min_year == max_year :
    raise ExamException('la serie è incompleta poiché contiene i dati relativi ad un solo anno e non è utilizzabile')

  #Controllo che first_year e last_year sono compresi nell'intervallo degli anni
  if first_year < min_year or last_year > max_year:
    raise ExamException('I parametri first_year e last_year sono fuori dall\'intervallo temporale della serie storica')
  
  #creo la lista annidata new_time_series che contiene le date convertite a interi, e il numero dei passeggeri che devono essere interi positivi, altrimenti salto la "riga"

  #uso il flag intero_positivo per fare il controllo sui valore
  new_time_series = []
  for line in time_series:
    new_row = []
    intero_positivo= True
    for i,element in enumerate(line):
        if i == 0:
          element=element.split('-')
          new_row.append(int(element[0]))
          new_row.append(int(element[1]))
        if i == 1:
          if element<= 0:
            intero_positivo= False
          new_row.append(element)
          
    if intero_positivo:
      new_time_series.append(new_row)   

  #months_values è una lista annidata che contiene i valori del numero di passeggeri per ogni mese
  months_values = [[] for i in range(12)]
  #Scorro gli elementi di new_time_series 
  for year,month, value in new_time_series: 
    #Verifico che l'anno sia contenuto nell'intervallo temporale che sto considerando
    if first_year <= year <= last_year: 
       months_values[month - 1].append(value)
      
  #Preparo la lista che contiene le variazioni medie mensili
  avg_monthly_differences = []

  #month_list corrisponde a tutti le misurazioni per un singolo mese
  for month_list in  months_values:
    #variations_for_month contiene le differenze tra le misurazioni del numero di passeggeri
    variations_for_month = []
    for i in range(len(month_list)):
      if i+1 < len(month_list):
        diff = month_list[i+1]-month_list[i]
        variations_for_month.append(diff)
    

    #Se per un mese non ci sono misurazioni o ce nè una sola la variazione media è 0

    if variations_for_month == []:
      avg_monthly_differences.append(0)

    #Se ho esattamente due misurazioni per un mese (per un intervallo di due anni o più)
    if len(variations_for_month) == 1:
      avg_monthly_differences.append(variations_for_month[0])

    #Se ho più di due misurazioni per un mese (per un intervallo maggiore di due anni)
    if len(variations_for_month) > 1:
      average = sum(variations_for_month)/len(variations_for_month)
      avg_monthly_differences.append(average) 
      
    
  return avg_monthly_differences
      

