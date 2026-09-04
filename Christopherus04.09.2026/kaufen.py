def kaufen(artikel, preis, anzahl):
    gesamtpreis = preis * anzahl
    print(f"Ich kaufe {anzahl}x {artikel} für insgesamt {gesamtpreis} Euro")

if __name__ == "__main__":
    artikel = "Schokolade"
    preis = 1.5
    anzahl = 3

    kaufen(artikel, preis, anzahl)