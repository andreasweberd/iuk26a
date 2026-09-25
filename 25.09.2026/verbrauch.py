# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def verbrauch(liter, km):
    # Use a breakpoint in the code line below to debug your script.
    rechnung = liter/km*100
    return rechnung




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    liter = float(input("Wie viele liter hast dur verbraucht?"))
    km = float(input("Wie viele km bist du gefahren="))
    rechnung = verbrauch(liter, km)
    print(f"Das Auto hat einen Verbrauch von {rechnung} Litern")


    if rechnung > 8:
        print("Es ist nicht sparsam")

    else:
        print("Es ist sparsam")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
