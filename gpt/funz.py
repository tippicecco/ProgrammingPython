# Costruttore, associo un nome mnemonico alla funzione,
# e gli estremi dell'intervallo
class Function: 
  def __init__(self, name, a, b):
    # nome funzione
    self.name = name
    # intervallo di riferimento
    self.a = a
    self.b = b

# Funzioni ausiliarie: stampa nome
  def printname(self):
    print("Function:", self.name, "tra [", self.a, ";", self.b, "]")

# Funzioni ausiliarie: stampa intervallo di valori
  def prettyprint(self, message, values):
    drop = False
    if (type(values) is list and len(values) > 10):
        drop = True
        values = values[1:10]
        values = values + ["..."]
    if (not drop):
        print("------")
    else:
        print("------ (mostro solo i primi 10 valori)")
    print(message, "->", values)
    print("------\n")

# metodo che risolve il problema algebrico descritto sopra
  def min_value(self, delta_x=0.5):
    print("Calcolo valore più vicino a 0")
    self.printname()

    # range di calcolo da a a b, con step delta_x
    x_start = self.a
    x_end = self.b
    i = 0

    # f_x memorizza f(x)
    f_x = []
    # abs_f_x memorizza |f(x)|
    abs_f_x = []
    x = []

    # valuto la funzione in punti all'interno di [a, b]
    # che distano tra loro delta_x
    while (x_start + i * delta_x) < x_end:
        this_x = x_start + i * delta_x

        # calcolo quanto vale la funzione nel punto di ascissa this_x
        this_fx = self.eval(this_x)

        x = x + [this_x]
        f_x = f_x + [this_fx]
        abs_f_x = abs_f_x + [abs(this_fx)]

        i = i + 1

    self.prettyprint("Dominio x", x)
    self.prettyprint("Funzione f(x)", f_x)
    self.prettyprint("Valore assoluto |f(x)|", abs_f_x)

    # per cercare il valore più vicino a 0 guardo i valori assoluti
    # all'indice in cui trovo il minimo ho trovato il valore che è più vicino a 0
    # assumo che la posizione 0 sia il minimo inizialmente
    x_min = 0
    for i in range(1, len(abs_f_x)):
        # se trovo un valore più piccolo del minimo corrente
        if abs_f_x[i] < abs_f_x[x_min]:
            # l'indice del minimo è i
            x_min = i

    print("L'elemento più vicino a 0 x =", x[x_min], "con f(x) =", self.eval(x[x_min]))


# Metodo di valutazione - pass!
  def eval(self, x):
     pass
class Retta(Function):
  def __init__(self, a, b, m, q):
# inizializzo la super-classe (funzione su intervallo)
    super().__init__("Retta", a, b)
# aggiungo come attributi coefficiente angolare e intercetta
    self.m = m
    self.q = q
  def printname(self):
  # chiamo il metodo omonimo della classe madre
    Function.printname(self)
   # aggiungo funzionalità
    print("Coeff angolare m = ", self.m, " e intercetta q = ", self.q)
# implemento eval sfruttando la forma funzionale della retta
# ovvero f(x) = m*x + q
  def eval(self, x):
    return self.m * x + self.q
#es utilizzo
bisettrice = Retta(-3, 33, 1, 0)
bisettrice.min_value(delta_x = 1)