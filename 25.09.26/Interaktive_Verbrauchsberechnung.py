def Verbrauch(Liter, Kilometer):
    Rechnung = Liter/Kilometer*100
    return Rechnung


if __name__ == "__main__":
    Liter = float(input("Wie viele Liter hast du verbraucht? "))
    Kilometer = float(input("Wie viele Kilometer hast du verbraucht? "))
    Rechnung = Verbrauch(Liter, Kilometer)
    print(f"Das Auto hat einen Verbrauch von {Rechnung:.2f} Litern.")


    if Rechnung > 8:
        print(f"Darum ist es nicht sparsam.")

    else:
        print(f"Darum ist es sparsam.")