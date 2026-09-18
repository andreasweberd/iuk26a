def berechne_bild(breite, hoehe, farbtiefe):
    groesse_in_bits = breite * hoehe * farbtiefe

    groesse_in_bytes = groesse_in_bits / 8
    groesse_in_mib = groesse_in_bytes / (1024 * 1024)

    return groesse_in_mib

def main():
    bildbreite = 1025
    bildhoehe = 680
    farbtiefe = 16

    ergebnis = berechne_bild(bildbreite, bildhoehe, farbtiefe)

    print(f"Ein Bild mit {bildbreite}x{bildhoehe} Pixeln und einer Farbtiefe von "
          f"{farbtiefe} Bits benötigt {ergebnis:} MiB Speicherplatz.")

if __name__ == "__main__":
    main()