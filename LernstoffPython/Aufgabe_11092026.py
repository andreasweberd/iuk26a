def kaufen(waskaufeich, preis, anzahl):
    print(f"Ich kaufe {anzahl}x {waskaufeich} für insgemsamt {preis} Euro")

if __name__ == "__main__":
    eingabe = input("Wie viele Teile Schokolade möchtest du (als int): ")
    anzahl = int(eingabe)
    feste_Zahl = int (3)
    preis = anzahl * feste_Zahl
    artikelname = "Schokolade"
    kaufen(artikelname, preis, anzahl)