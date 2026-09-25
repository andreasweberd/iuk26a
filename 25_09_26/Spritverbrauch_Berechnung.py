def berechne_Verbrauch(kilometer, liter):
    verbrauch = liter / kilometer * 100
    return verbrauch


if __name__ == "__main__":
    kilometer = float(input("Wieviele kilometer bist du gefahren? "))
    liter = float(input("Wieviele Liter bist du gefahren? "))

    verbrauch = berechne_Verbrauch(kilometer, liter)
    print(f"dein verbrauch beträgt {verbrauch}")
    if (verbrauch > 8):
        print("sparsam")
    else:
        print("nicht sparsam")
