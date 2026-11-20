#getraenkeautomat nach pap

inventory = [20,0,0,77,9,88,888888,111]
prices = [5.20,6.80,7,8,1,2,3,4,56,43]

def process_client_order(product_id):

    lagerbestand = inventory[product_id]

    if lagerbestand == 0 :
         print("ERROR")
         return

    preis = prices[product_id]
    einwurf = 0
    print("Preis " + str(preis))
    while einwurf < preis:
         muenze = input("Gib Geld")
         if muenze >= 0.10 and muenze <= 2:
              einwurf = einwurf + muenze 
    abbruch = input("Abbruch")
    if abbruch == "ja": return

    print("hier dein Getraenk")

    inventory[product_id] = lagerbestand -1
    print("Hier Restgeld: " + str(einwurf - preis))
    return

if __name__ == "__main__":
     process_client_order(0)
     
#array waere sowas: a = [0,1,2,3]