def berechne_bild(Breite, Höhe, Farbtiefe):
    Bits = Breite*Höhe*Farbtiefe
    Bytes = Bits/8
    Kibibytes = Bytes/1024
    Mebibytes = Kibibytes/1024
    return Mebibytes

if __name__ == "__main__":
    Dateigröße = berechne_bild(1025,680,16)
    print("Die Dateigröße ist: " + str(Dateigröße), "Mebibytes.")