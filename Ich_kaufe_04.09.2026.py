def kaufen(waskaufeich, preis, anzahl):
    gesamtpreis =  preis
    print(f"Ich kaufe ´{anzahl}x {waskaufeich} für insgesamt {gesamtpreis} Euro.")

if __name__ == "__main__":
        anzahl = 5
        preis = 4.5
        artikelname= "schokolade"
        kaufen(artikelname, preis, anzahl)
