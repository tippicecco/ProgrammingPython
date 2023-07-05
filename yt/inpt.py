persona = {
  "nome": "luca",
  "cog": "mora"
}
operazione = ("add", "mod", "del", "exit")

def start():
  while True:
    operazione = input("Che operazione vuoi fare? (add, mod, del, exit): ")
    
    if operazione == "add":
      x = input("Aggiungi elemento: chiave, valore ")
      aggiungi(*x.split(","))
    elif operazione == "mod":
      x = input("Seleziona la chiave da modificare: ")
      modifica(x)
    elif operazione == "del":
      x = input("Seleziona la chiave da eliminare: ")
      elimina(x)
    elif operazione == "exit":
      break
    else:
      print("Operazione non valida. Riprova.")

def aggiungi(chiave, valore):
  persona[chiave] = valore
  print(persona)

def modifica(chiave):
  valore = input("Immettere il nuovo valore: ")
  persona[chiave] = valore
  print(persona)

def elimina(chiave):
  if chiave in persona:
    del persona[chiave]
    print(f"Elemento con chiave '{chiave}' eliminato.")
  else:
    print(f"La chiave '{chiave}' non esiste.")

start()
