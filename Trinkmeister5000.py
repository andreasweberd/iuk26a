produkte = [{"nummer": i, "vorraetig": 2, "preis": 2.5} for i in range(1, 51)]


def produktAuswahl():
    eingabe = int(input("Produktnummer eingeben: "))
    
    if eingabe == 0000:
        return

    for produkt in produkte:
        if eingabe == produkt["nummer"] and produkt["vorraetig"] > 0:
            print(produkt["preis"])
            print(produkt)
            bezahlProzess(produkt["preis"], produkt["nummer"])
    produktAuswahl()

def bezahlProzess(preis, nummer):
    einwurf = 0.0
    while einwurf < preis:
        muenze = int(input("Welche Münze wollen sie einwerfen? 1: 10ct, 2: 20ct, 3: 50ct, 4: 1€, 5: 2€, 6: Abbruch "))
        match muenze:
            case 1:
                einwurf = round(einwurf + 0.1, 2)
            case 2:
                einwurf = round(einwurf + 0.2, 2)
            case 3:
                einwurf = round(einwurf + 0.5, 2)
            case 4:
                einwurf = round(einwurf + 1.0, 2)
            case 5:
                einwurf = round(einwurf + 2.0, 2)
            case 6:
                produktAuswahl()
                return
            case _:
                print("Ungültiger Einwurf")
        if einwurf < preis:
            print(f"{preis - einwurf:.2f}€ fehlen")
            
    print(f"Hier ist ihr Produkt.\nSie erhalten {einwurf - preis:.2f}€ Wechselgeld")
    produkte[nummer - 1]["vorraetig"] -= 1
    print(produkte[nummer - 1]["vorraetig"])

    
    

if __name__ == "__main__":
    produktAuswahl()


