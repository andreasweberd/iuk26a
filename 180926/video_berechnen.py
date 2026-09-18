def berechne_bild(breite: int, hoehe: int, farbtiefe: int) -> float:

    groesse_bits = breite * hoehe * farbtiefe
    groesse_mib = groesse_bits / (1024 * 1024 * 8)
    return groesse_mib


def berechne_audio(abtastrate: int, bittiefe: int, kanaele: int, zeit_in_sekunden: float) -> float:

    groesse_bits = abtastrate * bittiefe * kanaele * zeit_in_sekunden
    groesse_mib = groesse_bits / (1024 * 1024 * 8)
    return groesse_mib


def berechne_video(
    breite: int,
    hoehe: int,
    farbtiefe: int,
    fps: int,
    abtastrate: int,
    bittiefe: int,
    kanaele: int,
    zeit_in_sekunden: float,
) -> tuple[float, float]:

    ein_bild_mib = berechne_bild(breite, hoehe, farbtiefe)

    gesamte_bild_mib = ein_bild_mib * fps * zeit_in_sekunden

    audio_mib = berechne_audio(abtastrate, bittiefe, kanaele, zeit_in_sekunden)

    gesamt_mib = gesamte_bild_mib + audio_mib
    gesamt_gib = gesamt_mib / 1024

    return gesamt_mib, gesamt_gib


def main() -> None:

    breite = 1025
    hoehe = 680
    farbtiefe = 16

    ergebnis_bild_mib = berechne_bild(breite, hoehe, farbtiefe)
    print(
        f"Ein Bild mit der Größe von {breite}x{hoehe} Pixeln und einer Farbtiefe von "
        f"{farbtiefe} Bit benötigt unkomprimiert {ergebnis_bild_mib:.2f} MiB Speicherplatz."
    )

    abtastrate_audio = 44100
    bittiefe_audio = 16
    kanaele_audio = 2
    zeit_audio = 10

    ergebnis_audio_mib = berechne_audio(abtastrate_audio, bittiefe_audio, kanaele_audio, zeit_audio)
    print(
        f"Eine Audiodatei ({abtastrate_audio} Hz, {bittiefe_audio} Bit, {kanaele_audio} Kanäle, "
        f"{zeit_audio}s) benötigt unkomprimiert {ergebnis_audio_mib:.2f} MiB Speicherplatz."
    )


    be_breite = 1920
    be_hoehe = 1080
    be_farbtiefe = 24
    be_fps = 30
    be_abtastrate = 48000
    be_bittiefe = 16
    be_kanaele = 2
    be_zeit = 60

    ergebnis_video_mib, ergebnis_video_gib = berechne_video(
        be_breite, be_hoehe, be_farbtiefe, be_fps,
        be_abtastrate, be_bittiefe, be_kanaele, be_zeit,
    )

    print(
        f"Ein {be_zeit}-sekündiges Full-HD-Video ({be_breite}x{be_hoehe} Pixel, {be_fps} fps) "
        f"inklusive 2-Kanal-Audio benötigt unkomprimiert {ergebnis_video_mib:.2f} MiB, "
        f"was {ergebnis_video_gib:.2f} GiB entspricht."
    )


if __name__ == "__main__":
    main()