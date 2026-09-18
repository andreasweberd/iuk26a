def berechne_bild(breite, hoehe, farbtiefe):
    # Dateigröße in Bits berechnen
    groesse_bits = breite * hoehe * farbtiefe

    # Umrechnung von Bits in Mebibyte (MiB)
    # 1 Byte = 8 Bits, 1 MiB = 1024 * 1024 Bytes = 1.048.576 Bytes
    # 1 MiB = 1.048.576 * 8 Bits = 8.388.608 Bits
    groesse_mib = groesse_bits / (1024 * 1024 * 8)

    return groesse_mib


def main():
    # Aufruf der Funktion mit den vorgegebenen Werten
    breite = 1025
    hoehe = 680
    farbtiefe = 16

    ergebnis_mib = berechne_bild(breite, hoehe, farbtiefe)

    # Ausgabe des Ergebnisses mit einem formatierten Satz
    print(
        f"Ein Bild mit der groeße von {breite}x{hoehe} Pixeln und einer Farbtiefe von {farbtiefe} Bit benötigt unkomprimiert {ergebnis_mib} MiB Speicherplatz.")


if __name__ == "__main__":
    main()