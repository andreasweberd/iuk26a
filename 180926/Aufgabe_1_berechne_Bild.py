def berechne_bild(breite, hoehe, farbtiefe):
    groesse_bits = breite * hoehe * farbtiefe
    groesse_mib = groesse_bits / (8 * 1024 * 1024)
    return groesse_mib



if __name__ == "__main__":
        breite = 1025
        hoehe = 680
        farbtiefe = 16

        ergebnis_mib = berechne_bild(breite, hoehe, farbtiefe)

        print(f"Die Dateigroesse des Bildes ist ({breite}x{hoehe} Pixel, {farbtiefe} Bit Farbtiefe) beträgt ca. {ergebnis_mib:.4f} MiB.")