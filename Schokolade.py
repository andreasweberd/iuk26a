def kaufen(waskaufeich, preis, anzahl):
    gesamtpreis = anzahl * preis
    print(f"Ich kaufe {anzahl}x {waskaufeich} für ingesamt {gesamtpreis} Euro.")

if __name__ == "__main__":
    anzahl = 5
    preis = 1.5
    artikelname = "Schokolade"
    kaufen(artikelname, preis, anzahl)