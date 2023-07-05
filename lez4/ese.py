class CSVFile:
    def __init__(self, file_name):
        self.name = file_name
        self.canread = True  
        try:
            self.csvfile = open(file_name, "r")
            self.csvfile.readline()
        except Exception:
            self.canread = False
            print("Errore nella lettura del file.")

    def get_data(self):
        if not self.canread:
            return None
        data_list = []
        for line in self.csvfile:
            line = line.strip()  # Rimuove eventuali spazi bianchi iniziali o finali
            elements = line.split(",")
            data_list.append(elements)
        return data_list
csv_file = CSVFile("shampu.csv")
print(csv_file.name)  # Stampa il nome del file

data = csv_file.get_data()  # Ottiene i dati come lista di liste
print(data)  # Stampa i dati del file CSV
