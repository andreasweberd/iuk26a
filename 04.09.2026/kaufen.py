def kaufen(artikel, preis, anzahl):
    print (f"Ich kaufe {anzahl}x {artikel} fuer insgesamt {anzahl * preis} Euro")


if __name__ == "__main__":
    artikel = "Brot"
    preis = 4
    anzahl = 5

    kaufen(artikel , preis , anzahl)


# schreibe eine Funktion kaufen(artikel,preis,anzahl), 
# die funktion soll berechnen, wie viel der einkauf insgesamt kostet,
# die funktion soll folgenden text auf der konsole ausgeben:
# "ich kaufe 3x schokolade fuer insgesamt 4,5 euro"
# erstelle im einsprungpunkt die variaben fuer artikelname, preis und anzahl, rufe die fumtion mit deinen variablen als parameer auf