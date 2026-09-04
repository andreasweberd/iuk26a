def kaufen(artikel, preis, anzahl):
    endpreis = preis * anzahl
    print(f"Ich kaufe {anzahl}x {artikel} für insgesamt {endpreis}€.")


if __name__ == "__main__":
    artikelname = ("Schokolade")                    #Schokolade = string
    preis = 4.5                                     #preis = float
    anzahl = 3                                      #anzahl = int
    kaufen(artikelname, preis, anzahl)
