def separatore():
  print("--------------")
class Persona:
  
  def __init__(self, ruolo, nome, cognome):
    self.nome = nome 
    self.cognome = cognome 
    self.ruolo = ruolo
  def bonjour(self):
    print(self.ruolo, ":", self.nome, self.cognome)

      
class Studente(Persona):
  def __init__(self, nome, cognome, lista_corsi):
    super().__init__("Studente UNITS", nome, cognome)
    self.lista_corsi = lista_corsi
    self.n = len(lista_corsi)
  def bonjour(self):
    Persona.bonjour(self)

# stampo con un for
    for i in range(0, self.n):
      print("> Frequento il corso: ", self.lista_corsi[i])
# sotto-classe Docente con una lista di corsi
# memorizzo anche n, il numero dei corsi insegnati
  def copertura_totale(lista_di_docenti, studente):
    coperto = False  
    print("Ricerca copertura")
    separatore()
    # iterazione indeterminata: appena tutti i corsi sono coperti esco dall'iterazione
    corsi_da_verificare = studente.lista_corsi
    i = 0  
    while not coperto and i<len(lista_di_docenti):
    # creo un nuovo studente il cui attributo corsi
    # ha tutti i corsi che non sono stati coperti dai docenti esaminati fino ad ora
      obj_S_ast = Studente(studente.nome, studente.cognome, corsi_da_verificare)
    # calcolo i corsi che non sono coperti, oppure lista vuota
      copertura_docente = docente_copre_studente(lista_di_docenti[i], obj_S_ast)
      # se tutti i corsi sono stati coperti
      if(len(copertura_docente) == 0):
        coperto = True
      # se alcuni corsi ancora non sono coperti
      else:
        corsi_da_verificare = copertura_docente
      i = i + 1
    print("Ricerca con tutti i docenti completata")
    separatore()
class Docente(Persona):
  def __init__(self, nome, cognome, lista_corsi):
    super().__init__("Docente UNITS", nome, cognome)
    self.lista_corsi = lista_corsi
    self.n = len(lista_corsi)
  def bonjour(self):
    Persona.bonjour(self)
# stampo con un for
    for i in range(0, self.n):
      print("> Insegno il corso: ", self.lista_corsi[i])

def docente_copre_studente(docente, studente):
# Convenevoli
  print("Docente che esamino")
  separatore()
  docente.bonjour()
  print("\n Studente che esamino")
  separatore()
  studente.bonjour()
  print("\n Ricerca in corso...")
  separatore()
  
  corsi_trovati = True #flag se tutti corsi tr
  corsi_scoperti = []
  for i in range(0,self.n):
    corso_trovato = False
    j = 0
    while not corso_trovato and j< len(docente.lista_corsi):
      if (studente.lista_corsi[i] == docente.lista_corsi[j]):
        corso_trovato = True
      j = j + 1
  
    print('Corso ' + studente.lista_corsi[i] + ' -> '  + corso_trovato )
    corsi_trovati = corsi_trovati and corso_trovato
    if (not corso_trovato):
      corsi_scoperti = corsi_scoperti + [studente.lista_corsi[i]]
  
  if (corsi_trovati):
    print('tutti coperti')
  else:
   print('non tutti coperti')
   for i in range (0, len(corsi_scoperti) ):
     print(corsi_scoperti[i])
  
  
  

#utilizzo





  
doc1 = Docente( "GIULIONE", "C", ['Algebra', 'Geometria'])
doc2 = Docente("SARU", "C", ['Analisi', 'Statistica'])
doc3 = Docente("ASSANI", "C", ['Letteratura', 'Algebra', 'informatica'])

doc4 = Docente("ASSANI", "C", ['Algebra', 'Geometria', 'Analisi', 'Statistica', 'informatica'])

stu = Studente("CECCO", "C", ['Algebra', 'Geometria', 'Analisi', 'Statistica', 'informatica'])
listadoc = [doc1, doc2, doc3]
doc4.docente_copre_studente(stu)