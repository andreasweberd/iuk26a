
if __name__ == "__main__":
    km = input("Wie viele km bist du gefahren?\n")
    liter = input("Wie viele Liter hast du verbraucht?\n")
    Verbrauch = (int(liter)/int(km))*100
    print("Verbrauch: "+str(Verbrauch))
    if Verbrauch < 8:
        print("Verbrauch niedrig.")
    else:
        print("Verbrauch hoch.")
