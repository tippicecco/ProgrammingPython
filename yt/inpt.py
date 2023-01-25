persona = {
  "nome" : "luca" ,
  "cog" : "mora"
}
operazione = ("add", "mod", "del")
def start():
  operazione = input("cabbo voi fa babbo: ")
  if operazione == operazione[0]:
    x = input ("agg elem: chiave , valore ")
    aggiungi(x.split(","))
  elif operazione == operazione[1]:
    pass
  elif operazione == operazione[2]:
    pass

def aggiungi(*param):
  chiave = param[0]
  valore = param[1]
  persona[chiave] = valore
  print(persona)

start()
