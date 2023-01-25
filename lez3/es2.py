
# Inizializzo una lista vuota per salvare i valori

def sumlist(my_file):
  value=0
  for line in my_file:
 # Faccio lo split di ogni riga sulla virgola
    elements = line.split(',')
    if elements[0] != 'Date':
 # Setto la data e il valore
      #date = elements[0]
      n = float(elements[1])
      value =  value + n
  return value

my_file = open ('shampoo_sales.csv', 'r')
my_file.readline()
print(sumlist(my_file))
#print('val: {}'.format(no))
 # Aggiungo alla lista dei valori questo valore 
my_file.close()