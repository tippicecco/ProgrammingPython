class Persona:
  def __init__(self,ruolo,nome,cognome):
    
    self.ruolo = ruolo
    self.nome = nome
    self.cognome = cognome
    
    
    
  def bonjour(self):
    print(self.ruolo,": ",self.nome, self.cognome)
  
class Studente(Persona):
  def __init__(self, nome, cognome, liscor):
    super().__init__("stud UNITS", nome,cognome)
    
    self.lista = liscor
    self.n = len(self.lista)
  
  def bonjour(self):
    #ridef metodo bonjour persona
    Persona.bonjour(self)
    for i in range(0,self.n):
      print("Frequento er brutto corso de: ", self.lista[i])
class Docente(Persona):
  def __init__(self, nome, cognome, liscor):
    super().__init__("Doc UNITS", nome,cognome)
    
    self.lista = liscor
    self.n = len(liscor)
  
  def bonjour(self):
    #ridef metodo bonjour persona
    Persona.bonjour(self)
    
    for item in self.lista:
      print("Insegno er corso de: ",item)

  def doc_copre_stu(self,stud):
    lscop= list()
    for corsos in stud.lista:
      scop=True
      for corsod in self.lista:
        if (corsod == corsos):
          scop=False
      print("Corso ", corsos, "->", not scop)
      if(scop==True):
        lscop = lscop + [corsos]
    return lscop

class A:
  x=0
  y=""
  def __init__(self, n,s):
    self.x = n
    self.y = s
  def __str__(self):
    return "A : " + self.x + " e " + self.y

#myo = A("123","xyz")
#print(myo.__str__())
fra = Studente("fra","cecco",["basi dati","prob","eco"])
car = Docente("g","c",["progr","basi dati","prob"])
fra.bonjour()
car.bonjour()
st_scoperti = car.doc_copre_stu(fra) 
[print(i) for i in st_scoperti]

print("------")
for i in range(0,4):
  print (i)
