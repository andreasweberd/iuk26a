def kaufen(artikel, preis, anzahl):

    gesamtpreis = anzahl * preis
    print(f"ich kaufe {anzahl}x {artikel} für insgesamt {gesamtpreis} Euro." )


if __name__ == "__main__":

    anzahl = 3
    preis  = 4,5
    artikel = "Schokolade"

    kaufen(anzahl, preis, artikel)





