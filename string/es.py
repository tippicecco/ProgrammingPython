import random
x = '4568777 {}'
y= 15
z = "  mandi soi \"checo \" soi nassut al {2} soi alt {1} e soi ciccion {0} "
print(len(x))
print(type(y))
for car in "computer":
  print(car)
print(z.strip())
print(z.replace("o","3"))
print ( z.format(13,7.9,9))

i=0
while i<6:
  print(i)
  i+=1
print (i)
print ("\n\n-----PAUSE-------\n")
ciccio = ["ud","ts","go","pn"]
print (ciccio[-4:-2])
ciccio.append("br")
print(ciccio)
ciccio.insert(2,"mi")
cacco=["tn","ra"]
ciccio.extend(cacco)
print(ciccio)
ciccio.pop(1)
del ciccio[1:4]
print(ciccio)
print("e cumo scurin gli elements\n")
nra= random.randint(0,2)
i=0
[print(citta) for citta in ciccio if citta != "br"]
gabbo = [ "baggiggio" for citta in ciccio] 
print(gabbo)
ciccio.sort(reverse=False)
print(ciccio)