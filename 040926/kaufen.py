def kaufen(artikel,preis,anzahl):
    finalpreis = str(preis * anzahl)
    anzahlstr = str(anzahl)
    print("Ich kaufe "+anzahlstr+"x "+artikel+" für "+finalpreis+" Euro.")

if __name__ == "__main__":
    artikel = ""
    preis = 0
    anzahl = 0

    artikel = input("Was kaufe ich?\n")
    preis = float(input("Wie viel kostet es?\n"))
    anzahl = int(input("Wie viele kaufe ich?\n"))

    kaufen(artikel,preis,anzahl)
