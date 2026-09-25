


# Press the green button in the gutter to run the script.
if __name__ == '__main__':





    liter = float (input("Wie viel Liter ist im Tank? "))


    km  = float (input("wieviele km bist du gefahren? "))

    verbrauch = liter / km * 100

    print(f"der Verbrauch von dir ist: {verbrauch}")

    if verbrauch > 8.0:
        print("hoher Verbrauch")

    else :
        print("sparsam")
