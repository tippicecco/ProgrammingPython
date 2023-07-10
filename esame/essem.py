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
        # Aggiungo alla lista gli elementi della linea tranne la prima,perchè 
        #l'ho saltata con my_file.readline()
        
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
            # creo una lista che contiene Anno e Mese della data, che devono 
            #essere separati da '-' 
            data_list = element.split('-')
        
            #se la lista che indica la data non ha lunghezza 2 , cioè è nel 
            #formato Anno Mese ,la riga non è valida
            
            if len(data_list) != 2:  
              print('la data {} non è valida div2'.format(element))
              riga_valida = False
              break
            #ciclo gli elementi Anno e Mese di data_list
            for value in data_list :
              #se riesco a convertirli ad interi allora i valori sono  
              #corretti altrimenti il flag diventa false
              try :
                value=int(value)
              except Exception:
                riga_valida = False
                print('la data {} non è valida notint'.format(element))
                break

            # verifico se il mese è 
            if riga_valida:    
              if int(data_list[1]) < 1 or int(data_list[1])>12:
                riga_valida = False
                print('la data {} non è valida messee'.format(element))
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
      #controllo se sono presenti timestamp duplicati oppure fuori ordine
      lista_di_date = []
      for row in int_data:
        data_list = row[0].split('-')
        int_data_list=[]
        for value in data_list:
          int_data_list.append(int(value)) 
        lista_di_date.append(int_data_list)
        
      
        
      prev_year=lista_di_date[0][0]
      prev_month = lista_di_date[0][1]
      #print('prevm',prev_month)
      for i,row in enumerate(lista_di_date,1):
        if i>1:
          curr_year = row[0]
          
          curr_month = row[1]
          
          if curr_year - prev_year > 1 :
            raise ExamException('timestamp fuori ordine curr-prev')
          if curr_year < prev_year:
            raise ExamException('timestamp fuori ordine prev maggio')
          if prev_month >= curr_month and prev_year == curr_year:
            if prev_month == curr_month:
              raise ExamException('timestamp duplicato uguaglianza')
            raise ExamException('timestampfuori ordine mesi maggiori')
          prev_year = curr_year
          prev_month = curr_month

        
      
      my_file.close()     
      return int_data      


def compute_avg_monthly_difference(time_series, first_year, last_year):
  
  #se la lista che contiene la serie storica è vuota
  
  if time_series is None:
    raise ExamException('Errore, la lista è vuota ')

  if len(time_series) == 1:
    raise ExamException('Errore,la serie storica non è utilizzabile perché contiene una sola riga')
  if not isinstance(first_year,str):
    raise ExamException('la variabile first_year deve essere una stringa')
  if not isinstance(last_year,str):
    raise ExamException('la variabile last_year deve essere una stringa')

  #rimuovo gli eventuali spazi bianchi 
  first_year = first_year.strip()
  last_year = last_year.strip()

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
    
    

  if first_year >= last_year:
    raise ExamException('Errore,last_year deve essere maggiore di first_year ')

  
  first_date_list = time_series[0][0].split('-')
  min_year = int(first_date_list[0])
  
  
  last_date_list = time_series[-1][0].split('-')
  max_year = int(last_date_list[0])

  if  min_year == max_year :
    raise ExamException('la serie è incompleta poiché contiene i dati relativi ad un solo anno e non è utilizzabile')
  if first_year < min_year or last_year > max_year:
    raise ExamException('I parametri first_year e last_year sono fuori l\'intervallo temporale della serie storica')
  
 
  
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
  
  monthly_differences = [[] for i in range(12)]
  
  for year,month, value in new_time_series:  
    if first_year <= year <= last_year: 
      monthly_differences[month - 1].append(value)
      
  
  avg_monthly_differences = []
  
  for month_list in monthly_differences:
    variations_sum = []
    for i in range(len(month_list)):
      if i+1 < len(month_list):
        diff = month_list[i+1]-month_list[i]
        variations_sum.append(diff)
    print(variations_sum)

    if variations_sum == []:
      avg_monthly_differences.append(0)

    if len(variations_sum) == 1:
      avg_monthly_differences.append(variations_sum[0])
      
    if len(variations_sum) > 1:
      average = sum(variations_sum)/len(variations_sum)
      avg_monthly_differences.append(average) 
    
  return avg_monthly_differences
  

#RICODATI DI CANCELLARE IL MAIN!!!!
exfile = CSVTimeSeriesFile('data.csv')
print('Nome del file {}'.format(exfile.name))
timeseries = exfile.get_data()
print(timeseries)
print(compute_avg_monthly_difference(timeseries, '1952','1955'))