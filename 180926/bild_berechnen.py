def berechne_bild(breite, hoehe, farbtiefe):
    # Dateigröße in Bits berechnen
    groesse_bits = breite * hoehe * farbtiefe

    # Umrechnung von Bits in Mebibyte (MiB)
    groesse_mib = groesse_bits / (1024 * 1024 * 8)

    return groesse_mib


def berechne_audio(abtastrate, bittiefe, kanaele, zeit_in_sekunden):
    # Dateigröße in Bits berechnen
    groesse_bits = abtastrate * bittiefe * kanaele * zeit_in_sekunden

    # Umrechnung von Bits in Mebibyte (MiB)
    groesse_mib = groesse_bits / (1024 * 1024 * 8)

    return groesse_mib


def berechne_video(breite, hoehe, farbtiefe, fps, abtastrate, bittiefe, kanaele, zeit_in_sekunden):
    # 1. Größe für ein einzelnes Bild in MiB abrufen
    ein_bild_mib = berechne_bild(breite, hoehe, farbtiefe)

    # 2. Bildgröße mit den Bildern pro Sekunde (fps) und der Gesamtzeit multiplizieren
    gesamte_bild_mib = ein_bild_mib * fps * zeit_in_sekunden

    # 3. Audio-Größe in MiB abrufen
    audio_mib = berechne_audio(abtastrate, bittiefe, kanaele, zeit_in_sekunden)

    # 4. Gesamtgröße berechnen (Bild + Ton)
    gesamt_mib = gesamte_bild_mib + audio_mib
    gesamt_gib = gesamt_mib / 1024

    return gesamt_mib, gesamt_gib


def main():
    # --- BILD ---
    breite = 1025
    hoehe = 680
    farbtiefe = 16

    ergebnis_bild_mib = berechne_bild(breite, hoehe, farbtiefe)
    print(
        f"Ein Bild mit der Größe von {breite}x{hoehe} Pixeln und einer Farbtiefe von {farbtiefe} Bit benötigt unkomprimiert {ergebnis_bild_mib} MiB Speicherplatz.")

    # --- AUDIO ---
    abtastrate_audio = 44100
    bittiefe_audio = 16
    kanaele_audio = 2
    zeit_audio = 10

    ergebnis_audio_mib = berechne_audio(abtastrate_audio, bittiefe_audio, kanaele_audio, zeit_audio)
    print(
        f"Eine Audiodatei ({abtastrate_audio} Hz, {bittiefe_audio} Bit, {kanaele_audio} Kanäle, {zeit_audio}s) benötigt unkomprimiert {ergebnis_audio_mib} MiB Speicherplatz.")

    # --- VIDEO ---
    v_breite = 1920
    v_hoehe = 1080
    v_farbtiefe = 24
    v_fps = 30
    v_abtastrate = 48000
    v_bittiefe = 16
    v_kanaele = 2
    v_zeit = 60

    ergebnis_video_mib, ergebnis_video_gib = berechne_video(
        v_breite, v_hoehe, v_farbtiefe, v_fps,
        v_abtastrate, v_bittiefe, v_kanaele, v_zeit
    )

    # Ausgabe des Video-Ergebnisses
    print(
        f"Ein {v_zeit}-sekündiges Full-HD-Video ({v_breite}x{v_hoehe} Pixel, {v_fps} fps) inklusive 2-Kanal-Audio benötigt unkomprimiert {ergebnis_video_mib} MiB, was {ergebnis_video_gib} GiB entspricht.")


if __name__ == "__main__":
    main()