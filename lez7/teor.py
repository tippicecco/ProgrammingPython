# Funzione somma
from math import pi
def somma(a,b):
 return a+b
def circle_area(r):
  if r < 0:
    raise ValueError("The radius cannot be negative")
  if type(r) not  in [int, float]:
    raise TypeError("The radius cannot be different from int or float")
  return pi * (r ** 2)


  
uno = '5'
due = '8'
if uno is str:
  try:
    float(uno)
  except:
    raise Exception("è stata inserita una stringa inconvertibile")
if uno is str:
  try:
    float(due)
  except Exception as e:
    print("è stata inserita una stringa inconvertibile, tipo errore {}". format(e))

if not somma(1,1) == 2:
 raise Exception('Test 1+1 non passato')
if not somma(1.5,2.5) == 4:
 raise Exception('Test 1.5+2.5 non passato')