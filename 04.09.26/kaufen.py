def kaufen(Artikel, Preis, Anzahl):
    Gesamtpreis = Anzahl * Preis
    print(f"Ich kaufe {Anzahl}x {Artikel} für insgesamt {Gesamtpreis} Euro.")


if __name__ == "__main__":
    Artikel = "Schokolade"
    Preis = 4.5
    Anzahl = 5
    kaufen(Artikel, Preis, Anzahl)
