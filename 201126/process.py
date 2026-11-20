def process_client_ordner(product_id):

    lagerbestand = inventory[product_id]

    if lagerbestand == 0 :
        print("ERROR")
        return
    preis = price[product_id]
    einwurf = 0
    print("PREIS" + str(preis))
    while einwurf < preis :
        muenze = input("GIB GELD")
        if muenze >= 0.10 and muenze <= 2 :
            einwurf = einwurf + muenze
    abbruch = input("ABBRUCH")
    if abbruch == "ja": return

    print("hier dein Getränk")

    inventory[product_id] = lagerbestand -1
    print("Ihr Restgeld: " + str(einwurf - price))
    return




if __name__ == "__main__":
    inventory = []
    price = []

