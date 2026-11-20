
inventory = [5, 10, 15, 20, 25]
prices = [1.5, 1.75, 2, 2.5]
def process_client_order(product_id):

    lagerbestand = inventory[product_id]

    if lagerbestand == 0 :
        print("ERROR")
        return
    preis = prices[product_id]
    einwurf = 0
    print("Preis" + str(preis))
    while einwurf < preis:
        muenze = float(input("Gib Geld"))
        if muenze >= 0.10 and muenze <= 2:
            einwurf = einwurf + muenze
    abbruch =input("Abbruch")
    if abbruch == "ja": return

    print("hier dein Getränk")
    inventory[product_id] = lagerbestand -1
    print(" Hier restgeld: " + str(einwurf - preis))
    return


if __name__ == "__main__":
    process_client_order(0)
