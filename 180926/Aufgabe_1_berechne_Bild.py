def berechne_bild(breite, hoehe, farbtiefe):
    groesse_bits = breite * hoehe * farbtiefe
    groesse_mib = groesse_bits / (8 * 1024 * 1024)
    return groesse_mib



if __name__ == "__main__":
        breite = 1025
        hoehe = 680
        farbtiefe = 16

        ergebnis_mib = berechne_bild(breite, hoehe, farbtiefe)

        print(f"Das Ergebnis ist ({breite}x{hoehe} Pixel, {farbtiefe} Bit Farbtiefe) beträgt ca. {ergebnis_mib:.4f} MiB.")

def berechne_audio(Abtastrate, Bittiefe, Kanaele, Zeit_in_Sekunden):
    groesse_bits = Abtastrate * Bittiefe * Kanaele * Zeit_in_Sekunden
    groesse_mib = groesse_bits / (8 * 1024 * 1024)
    return groesse_mib

if __name__ == "__main__":
    Abtastrate = 44100
    Bittiefe = 16
    Kanaele = 2
    Zeit_in_Sekunden = 10

    ergebnis_mib = berechne_audio(Abtastrate, Bittiefe, Kanaele, Zeit_in_Sekunden)


def berechne_bild(breite, hoehe, farbtiefe):

    groesse_bits = breite * hoehe * farbtiefe

    groesse_mib = groesse_bits / (8 * 1024 * 1024)
    return groesse_mib


def berechne_audio(abtastrate, bittiefe, kanaele, zeit_in_sekunden):

    groesse_bits = abtastrate * bittiefe * kanaele * zeit_in_sekunden

    groesse_mib = groesse_bits / (8 * 1024 * 1024)
    return groesse_mib


def berechne_video(breite, hoehe, farbtiefe, fps, abtastrate, bittiefe, kanaele, zeit_in_sekunden):

    frame_mib = berechne_bild(breite, hoehe, farbtiefe)


    video_spur_mib = frame_mib * fps * zeit_in_sekunden


    audio_spur_mib = berechne_audio(abtastrate, bittiefe, kanaele, zeit_in_sekunden)


    gesamt_mib = video_spur_mib + audio_spur_mib

    gesamt_gib = gesamt_mib / 1024

    return gesamt_gib


if __name__ == "__main__":

    breite = 1920
    hoehe = 1080
    farbtiefe = 24
    fps = 30

    abtastrate = 48000
    bittiefe = 16
    kanaele = 2

    zeit_in_sekunden = 60


    bild_mib = berechne_bild(breite, hoehe, farbtiefe)
    print(f"Ein Einzelbild ({breite}x{hoehe}) benötigt: {bild_mib:.4f} MiB")


    audio_mib = berechne_audio(abtastrate, bittiefe, kanaele, zeit_in_sekunden)
    print(f"Eine Tonspur ({zeit_in_sekunden}s) benötigt: {audio_mib:.4f} MiB")

    video_gib = berechne_video(
        breite, hoehe, farbtiefe, fps,
        abtastrate, bittiefe, kanaele, zeit_in_sekunden
    )

    print(f"\nDas gesamte Video ({zeit_in_sekunden}s mit {fps} fps) benötigt: {video_gib:.4f} GiB")