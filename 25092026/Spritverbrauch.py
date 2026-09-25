if __name__ == "__main__":
    sprit = float(input("Gebe die verbrauchten Liter an:"))
    km = float(input("Gebe die gefahrenen Kilometer an:"))
    verbrauch = (sprit / km) * 100

    if verbrauch > 8:
        print(f"Der Spriverbrauch ist hoch und beträgt {verbrauch}l auf 100km.")

    else:
        print(f"Der Spritverbrauch ist niedrig und beträgt {verbrauch}l auf 100km.")


