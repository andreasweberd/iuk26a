def berechne_bild(breite, hoehe, farbtiefe):
    bits = breite * hoehe * farbtiefe
    MiB = bits / 8 / 1024 / 1024
    print(f"Die Bildgröße betragt {MiB} MiB.")


if __name__ == "__main__":
    breite = 1025
    hoehe = 680
    farbtiefe = 16
    berechne_bild(breite, hoehe, farbtiefe)
