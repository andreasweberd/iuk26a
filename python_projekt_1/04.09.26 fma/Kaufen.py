def kaufen(artikel,preis,anzahl):
    Endpreis=preis*anzahl
    print(f"Ich kaufe {anzahl}x {artikel} für insgesamt {Endpreis} Euro.")




if __name__=="__main__":
    anzahl = 5
    artikel = "Schokolade"
    preis = 1.5
    kaufen(artikel,preis,anzahl)


