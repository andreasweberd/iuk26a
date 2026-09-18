def berechne_bild(breite, hoehe, farbtiefe):

    dateigröße = breite * hoehe * farbtiefe

    dateigröße = dateigröße / 8
    dateigröße = dateigröße / 1024
    dateigröße = dateigröße / 1024

    print(f"Das Ergebnis ist {dateigröße}")


if __name__ == "__main__":

    breite = 1025
    hoehe = 680
    farbtiefe = 16

    berechne_bild(breite, hoehe, farbtiefe)

