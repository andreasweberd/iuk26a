inventory = [10,35,26,13,4]
prices = [2.5,4,3.25,6.99,1]

def process_client_order(product_id):

    Lagerbestand = inventory[product_id]

    if Lagerbestand == 0 :
        print ("ERROR")
        return
    Preis = prices[product_id]
    Einwurf = 0
    print("Preis " + str(Preis))
    while Einwurf < Preis:
        Münze = float(input("Gib Geld! "))
        if Münze >= 0.10 and Münze <= 2:
            Einwurf = Einwurf + Münze
    Abbruch = input("Abbruch")
    if Abbruch == "ja": return

    print("Hier dein Getränk.")

    inventory[product_id] = Lagerbestand -1
    print("Hier Restgeld: " + str(Einwurf - Preis))

    return




if __name__ == "__main__":
    process_client_order(0)