# Comandi di base
a = 10  # Assegnamento di una variabile
print(a)  # Stampa il valore di a

if a > 5:  # Condizione if-else
    print("a è maggiore di 5")
else:
    print("a è minore o uguale a 5")

for i in range(5):  # Ciclo for
    print(i)

# Principali oggetti
lista = [1, 2, 3, 4, 5]  # Lista
dizionario = {'nome': 'Mario', 'età': 25}  # Dizionario
insieme = {1, 2, 3, 4, 5}  # Insieme

print(lista[0])  # Accesso agli elementi della lista
print(dizionario['nome'])  # Accesso ai valori del dizionario

# Classi ed ereditarietà
class Veicolo:
    def __init__(self, marca, modello):
        self.marca = marca
        self.modello = modello

    def info(self):
        print("Veicolo:", self.marca, self.modello)

class Automobile(Veicolo):
    def __init__(self, marca, modello, porte):
        super().__init__(marca, modello)
        self.porte = porte

    def info(self):
        super().info()
        print("Porte:", self.porte)

veicolo1 = Veicolo("Fiat", "Panda")
veicolo1.info()

auto1 = Automobile("Ford", "Focus", 5)
auto1.info()

# Funzioni
def somma(a, b):
    return a + b

risultato = somma(3, 4)
print(risultato)
