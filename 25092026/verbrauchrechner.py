def verbrauch():

    liter = float(input("Wie viele Liter hast du verbraucht? "))
                  
    kilometer = float(input("Wie vile Kilometer bist du gefahren? "))

    sprit_verbrauch = (liter / kilometer) * 100

    print(f"Du hast einen Verbrauch von {sprit_verbrauch} l/100km")
    return sprit_verbrauch

if __name__ == "__main__":
    sparsam = verbrauch()

    if sparsam <= 5:
        print("Dein Verbrauch ist sehr niedrig. Super!")

    #else: 
    # print("Dein Verbrauch ist hoch. Nicht gut!")

    if sparsam > 5:
        print("Dein Verbrauch ist hoch. Nicht gut!")

