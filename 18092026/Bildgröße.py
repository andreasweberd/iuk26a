def berechne_bild(breite, hoehe, farbtiefe):
    bits = breite * hoehe * farbtiefe
    MiB = bits / 8 / 1024 / 1024
    print(f"Die Bildgröße beträgt {MiB} MiB.")

if __name__ == "__main__":
    berechne_bild(1025, 680, 16)