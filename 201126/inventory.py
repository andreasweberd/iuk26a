inventory = [20,50,45,30,22]
price = [2,2.50,3.50]



def process_client_order(product_id):
    lagerbestand = inventory[product_id]

    if lagerbestand == 0 :
        print("Error")
        return
    preis =price[product_id]
    einwurf = 0
    print("preis" + str(preis))
    while einwurf < preis :
        muenze = float(input("Gib Geld"))
        if muenze >= 0.10 and muenze <=2:
            einwurf = einwurf + muenze

    abbruch = input("Abbruch")
    if abbruch == "ja": return

    print("hier dein Getränk")

    inventory[product_id] = lagerbestand -1
    print("Hier restgeld:" + str(einwurf - preis))
    return

if __name__ == "__main__":
    process_client_order(1)
