mio_dict = {"mia chiave":"mio valore", "age": 27, 3.14 : "pi greco", "primi" : [1,2,3,5,7] }
print(type(mio_dict))
print((mio_dict))
print("il primo valore della chiave mia \n chiave:  {}".format(mio_dict["mia chiave"]))
print(29 in mio_dict)
if "spam" in mio_dict:
  pass
else:
  mio_dict["nuova chiave"] = "spam"
print((mio_dict))
del mio_dict["mia chiave"]
print((mio_dict.keys()))
print((mio_dict.values()))
print((mio_dict.items()))
#trovare i valori
mio_dict["mia chiave"] = mio_dict.get(3.14, "chiave non trovata")
print(mio_dict.get("agess", "chive non trovata"))
#se trovo chiave non faccio niente altrimenti inserisco un nuovo campo
mio_dict.setdefault("sesso", "MF")
print(mio_dict)