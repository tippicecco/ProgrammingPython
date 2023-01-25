def sum_list(my_list):
  if len(my_list)==0:
    return None
  return sum(my_list)
my_list=[6,7,8,6,5,7]
a=sum_list(my_list)
print('a vale:{} '.format(a)) 
for i,item in enumerate(my_list): #ciclo per vedere la posizione e il valore di elem
  print('posiz {}: {}, {} '.format(i,item, my_list))
  