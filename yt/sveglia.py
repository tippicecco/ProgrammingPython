import time

print("Impostare l'ora di sveglia (hh:mm):")
ora_sveglia = input()

print("Impostare la durata della sveglia (in minuti):")
durata_sveglia = int(input())

print("La sveglia verrà attivata alle", ora_sveglia)

while True:
    ora_corrente = time.strftime("%H:%M")
    if ora_corrente == ora_sveglia:
        print("È ora di alzarsi!")
        time.sleep(durata_sveglia * 60)
        break
    time.sleep(60)
