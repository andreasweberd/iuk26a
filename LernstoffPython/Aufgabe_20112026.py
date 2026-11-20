def process_client_order(product_id):
    inventory = [x for x in range(51)]
    lagerbestand  = inventory[product_id]         #lager bestand = wie viel davon ist drin 0 oder mehr

    if lagerbestand == 0:
        print("ERROR")
        return
    a = 0
    prices = [a for x in inventory]
    preis = prices[product_id]
    einwurf = 0
    print("Preis" + str(preis))

    while einwurf < preis:
        muenze = float(input("Gib Geld"))
        if muenze >= 0.10 and muenze <= 2:
            einwurf = einwurf + muenze

    abbruch = input("Abbruch")
    if abbruch == "ja": return

    print("hier dein Gedränk")


    inventory[product_id] = lagerbestand -1
    print("Hier restgeld: " + str(einwurf - preis))
    return

if __name__ == "__main__":
    process_client_order(2)
