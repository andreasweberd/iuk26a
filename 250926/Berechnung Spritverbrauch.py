if __name__ == '__main__':
    gefahrene_km = float(input("Wie viele km bist du gefahren?"))
    liter = float(input("Wie viele liter hast du verbraucht?"))

    verbauch = (liter / gefahrene_km) * 100

    print(f" Verbrauch auf 100 km{verbauch:.2f} Liter")

    if verbauch > 8:
        print("Hoher verbauch!")
    else:
        print("niedriger Verbrauch")