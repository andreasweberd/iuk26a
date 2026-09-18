def berechne_bild(breite, hoehe, farbtiefe):
    Bits = breite * hoehe * farbtiefe
    Bytes = Bits/8
    Kibibytes = Bytes/1024
    Mibibytes = Kibibytes/1024
    return Mibibytes

if __name__ == "__main__":
    Ergebnis = berechne_bild(1025,680,16)
    print("Das Ergebnis ist: " + str(Ergebnis))
