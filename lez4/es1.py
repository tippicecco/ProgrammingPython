class CSVFile():
  def __init__(self, file_name):
      self.name = file_name
  
  def __str__(self):
    return '{}'.format(self.name)
  def get_data(self,shampoo):
    lista=[]
    for line in shampoo:
        lista.append(line)
    print(lista)
      
  
     
shampoo = open('shampu.csv', 'r')
csvfile = CSVFile(shampoo)
print(csvfile)
print(csvfile.name)
csvfile.get_data(shampoo)

  