def berechne_bild(breite, hoehe, farbtiefe):
    Bits = breite * hoehe * farbtiefe
    Bytes = Bits / 8
    Kibibytes = Bytes / 1024
    Mebibytes = Kibibytes / 1024
    return Mebibytes

if __name__ == "__main__":
    Ergebnis_berechne_bild = berechne_bild(1025, 680, 16)
    print(f"Das Ergebnis ist: {Ergebnis_berechne_bild} MiB")
