def main():
    # Eingabe
    km = float(input("Gefahrene km: "))
    liter = float(input("Liter im Tank: "))

    # Berechnung
    verbrauch = (liter / km) * 100

    # Ausgabe
    print(f"Verbrauch: {verbrauch} Liter/100km")

    # Bedingung
    if verbrauch > 8:
        print("hoher Verbrauch")
    else:
        print("Sparsam")


# Einsprungspunkt
if __name__ == "__main__":
    main()