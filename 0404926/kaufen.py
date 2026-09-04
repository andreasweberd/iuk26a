def kaufen(artikel, preis, anzahl):
    gesamtpreis=preis*anzahl
    print(f"Ich kaufe {anzahl}x {artikel} für insgesamt {gesamtpreis} Euro.")

if __name__=="__main__":
    anzahl=5
    preis=4.5
    artikel="Schokolade"
    kaufen(artikel, preis, anzahl)