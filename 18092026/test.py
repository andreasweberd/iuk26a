# Funktion Aufgabe 1
def berechne_bild(breite, hoehe, farbtiefe):
    bild_bits = breite * hoehe * farbtiefe
    bild_MiB = bild_bits / 8 / 1024 / 1024
    print(f"Die Bildgröße beträgt {bild_MiB:.2f} MiB.")
    return bild_bits  # Gibt Bits für die Videoberechnung zurück

# Funktion Aufgabe 2
def berechne_audio(abtastrate, bittiefe, kanaele, zeit_in_sekunden):
    audio_bits = abtastrate * bittiefe * kanaele * zeit_in_sekunden
    audio_MiB = audio_bits / 8 / 1024 / 1024
    print(f"Die Audiogröße beträgt {audio_MiB:.2f} MiB.")
    return audio_bits  # Gibt Bits für die Videoberechnung zurück

# Funktion Aufgabe 3
def berechne_video(breite, hoehe, farbtiefe, fps, abtastrate, bittiefe, kanaele, zeit_in_sekunden):
    videospur_bits = berechne_bild(breite, hoehe, farbtiefe) * fps * zeit_in_sekunden
    audiospur_bits = berechne_audio(abtastrate, bittiefe, kanaele, zeit_in_sekunden)

    video_bits_gesamt = videospur_bits + audiospur_bits
    video_MiB = video_bits_gesamt / 8 / 1024 / 1024

    print(f"Die Videogröße beträgt {video_MiB:.2f} MiB.")


if __name__ == "__main__":
    print("--- Bildberechnung ---")
    berechne_bild(1025, 680, 16)

    print("\n--- Audioberechnung ---")
    berechne_audio(44100, 16, 2, 10)

    print("\n--- Videoberechnung ---")
    berechne_video(1920, 1080, 24, 30, 48000, 16, 2, 60)
