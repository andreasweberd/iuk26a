
inventory = [20,787,21,37,201,1010]
prices = [5.20,8.99,7.87,1.00,54.3]
artikel = ["apfel","monster","surface","gta6","PS5 Pro"]

def process_client_order (product_id):

    lagerbestand = inventory[product_id]

    if lagerbestand == 0
            print("ERROR")
            return
    preis = prices[product_id]
    einwurf = 0
    println("Preis" + str(preis))
    while einwurf < preis:
        muenze = float(input("Gib Geld"))
        if muenze >= 0.10 && muenze <= 2:
            einwurf = einwurf + muenze

    abbruch  = input("Gib Abbrechen")
    if abbruch == "Ja": return

    println("hier dein Getränk")

    inventory[product_id] = lagerbestand -1
    println("hier Restgeld:" + str(einwurf - preis))

    return

if __name__ == "__main__":
    process_client_order(2)