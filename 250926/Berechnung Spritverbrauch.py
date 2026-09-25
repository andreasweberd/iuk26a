if __name__ == '__main__':
    gefahrene_km = float(input("wie viel km bist du gefahren? "))
    liter = float(input("wie viel liter hast du verbraucht? "))

    verbrauch = (liter / gefahrene_km) * 100

    print(f"Verbrauch auf 100 km: {verbrauch:.2f} Liter")

    if verbrauch > 8:
        print("Hoher Verbrauch!")
    else:
        print("Sparsamer Verbrauch")