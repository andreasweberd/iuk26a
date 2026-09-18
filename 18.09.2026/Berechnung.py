# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def berechne_bild(breite, hoehe, farbtiefe):
    # Use a breakpoint in the code line below to debug your script.
    Bits = breite*hoehe*farbtiefe
    Bytes = Bits/8
    Kibibytes = Bytes/1024
    Mebibytes = Kibibytes/1024
    return Mebibytes

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    Ergebnis = berechne_bild(1025,680,16)
    print('Das Ergbnis ist:'  + str(Ergebnis))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
