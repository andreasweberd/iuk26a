def berechne_bild(breite,hoehe,farbtiefe):
    Bits = breite*hoehe*farbtiefe
    Kibibytes = Bits/1024
    Mebibytes = Kibibytes/1024
    return Mebibytes

if __name__ == "__main__":
    Ergebnis = berechne_bild(1025,680,16)
    print("Das Ergebnis ist: " + str(Ergebnis))
