inventory = [3]
prices = [4]


def processes_client_order(product_id):
    lagerbestand = inventory[product_id]

    if lagerbestand == 0:
        print("Grtänk nicht verfügbar")
        return
    preis = prices[product_id]
    einwurf = 0
    print("Preis: " + str(preis))
    while einwurf < preis:
        muenze = float(input("Bitte Geld einwerfen "))
        if 0.10 <= muenze <= 2:
            einwurf += muenze
    abbruch = input("Abbruch? Y/N")
    if abbruch == "Y": return
    print("Hier dein Getränk")
    inventory[product_id] = lagerbestand - 1
    rueckgeld = einwurf - preis
    print("Rückgeld: " + str(rueckgeld))
    return


if __name__ == "__main__":
    processes_client_order(0)
