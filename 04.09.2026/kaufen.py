def kaufen(artikel, anzahl, preis):
    gesamt = preis * anzahl
    print("Ich kaufe", anzahl, "x", artikel, "für insgesamt", gesamt, "Euro")


if __name__ == "__main__":
    artikel = "Schokolade"
    anzahl = 3
    preis = 1.50

    kaufen(artikel, anzahl, preis)