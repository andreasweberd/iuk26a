# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def kaufen(artikel, preis, anzahl):
    gesamtpreis = preis * anzahl
    print(f"Ich kaufe {anzahl}x {artikel} für insgesamt {gesamtpreis} Euro.")
    # Use a breakpoint in the code line below to debug your script.
     # Press Strg+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    artikel = "Schokolade"
    preis = 1.5
    anzahl = 5

    kaufen(artikel, preis, anzahl)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
