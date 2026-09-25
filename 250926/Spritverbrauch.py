def berechne_verbrauch(kilometer,liter):
    verbrauch = kilometer/liter * 100
    return verbrauch

if __name__ == '__main__':
    kilometer=float(input("wie viele kilometer bist du gefahren"))
    liter=float(input("wie viele liter hast du getankt?"))
    verbrauch= berechne_verbrauch(kilometer,liter)
    print(f"verbrauch: {verbrauch} liter pro 100 km")

    if verbrauch > 8:
        print("hoher verbrauch")
    else:
       print("niedriger verbrauch")