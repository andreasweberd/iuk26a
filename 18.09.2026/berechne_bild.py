def berechne_bild(breite, höhe, farbtiefe):

    Dateigröße = breite * höhe * farbtiefe 
    Bytes = Dateigröße/8 
    Kibibytes = Bytes/1024
    Mebibytes = Kibibytes/1024
    return Mebibytes


if __name__ == '__main__':

    breite = 1025 
    höhe = 680
    farbtiefe = 16

    Ergebniss = berechne_bild(breite, höhe, farbtiefe)

    print('Das Ergebnis ist: ' + str(Ergebniss))