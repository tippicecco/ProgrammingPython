def ordina(my_list):
  
  try:
    
    my_list.sort()
  except TypeError:
    print("non è permesso il confronto tra diversi tipi di variabili: ")
    trovato = False
    i = 0
    while (i< len(my_list)):
      k = 0
      a = my_list[i]
      while not trovato:
        if(type(my_list[k]) != type(a)):
          trovato = True
        else:
          k+= 1
      print("{} ".format(type(a)))
      i += 1
      
  else:
    print(my_list)
  lista_conv = []
  for item in my_list:
    
    try :
      item_convertito = float(item)
    except:
      #conversione str -> float
      if(len(item)==1 and type(item) != list):
        print('non posso convertire da stringa a float elemento {}'. format(item))
        #--
    else:
      if(type(item) == str):
        print("l\'elemento {} lo posso convertire a float".format(item))
      lista_conv.append(item_convertito)
  print(lista_conv)  
      
      
  
  

my_list1 = [[5,7], [1],  [3], [8]]
my_list = ['arturo', 'charlie',  'bobbie', 'daffy']
#print(len(my_list[0]))
ordina(my_list)