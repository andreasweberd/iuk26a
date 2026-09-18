def berechne_bild(breite, hoehe, farbtiefe):
    Bits = breite * hoehe * farbtiefe
    Bytes = Bits / 8
    Kibibytes = Bytes / 1024
    Mebibytes = Kibibytes / 1024
    return Mebibytes

if __name__ == "__main__":
    Ergebnis_berechne_bild = berechne_bild(1025, 680, 16)
    print(f"Das Ergebnis ist: {Ergebnis_berechne_bild} MiB")

def berechne_audio(abtastrate, bittiefe, kanaele, zeit_in_sekunden):
    groesse_bits = abtastrate * bittiefe * kanaele * zeit_in_sekunden
    groesse_mib = groesse_bits / (8 * 1024 * 1024)
    return groesse_mib

if __name__ == "__main__":
    abtastrate = 44100
    bittiefe = 16
    kanaele = 2
    zeit_in_sekunden = 10

    ergebnis_mib = berechne_audio(abtastrate, bittiefe, kanaele, zeit_in_sekunden)

    print(f"Das Ergebnis ist ({abtastrate}x{bittiefe}x{kanaele}x{zeit_in_sekunden}) beträgt ca. {ergebnis_mib}")


def berechne_video(Breite, Hoehe, Farbtiefe, fps, Abtastrate, Bittiefe, Kanaele, Zeit_in_Sekunden):
    ergebnis_frame_mib = berechne_bild(Breite, Hoehe, Farbtiefe)

    gesamt_video_mib = ergebnis_frame_mib * fps * Zeit_in_Sekunden

    gesamt_audio_mib = berechne_audio(Abtastrate, Bittiefe, Kanaele, Zeit_in_Sekunden)

    gesamt_dateigroesse_mib = gesamt_video_mib + gesamt_audio_mib

    return gesamt_dateigroesse_mib


if __name__ == "__main__":
    Abtastrate = 44100
    Bittiefe = 16
    Kanaele = 2
    Zeit_in_Sekunden = 10

    ergebnis_mib = berechne_audio(Abtastrate, Bittiefe, Kanaele, Zeit_in_Sekunden)
    print(f"Das Ergebnis ist beträgt ca. {ergebnis_mib:.4f} MiB.")

    Breite = 1920
    Hoehe = 1080
    Farbtiefe = 24
    fps = 30
    Abtastrate = 48000
    Bittiefe = 16
    Kanaele = 2
    Zeit_in_Sekunden = 60

    video_ergebnis_mib = berechne_video(Breite, Hoehe, Farbtiefe, fps, Abtastrate, Bittiefe, Kanaele, Zeit_in_Sekunden)

    print(f"Das Video-Gesamtergebnis beträgt ca. {video_ergebnis_mib:.4f} MiB.")


