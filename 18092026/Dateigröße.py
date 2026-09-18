#Funktion Aufgabe 1
def berechne_bild(breite, hoehe, farbtiefe):
    bild_bits = breite * hoehe * farbtiefe
    bild_MiB = bild_bits / 8 / 1024 / 1024
    print(f"Die Bildgröße beträgt {bild_MiB} MiB.")

#Funktion Aufgabe 2
def berechne_audio(abtastrate, bittiefe, kanaele, zeit_in_sekunden):
    audio_bits = abtastrate * bittiefe * kanaele * zeit_in_sekunden
    audio_MiB = audio_bits / 8 / 1024 / 1024
    print(f"Die Audiogröße beträgt {audio_MiB} MiB.")

if __name__ == "__main__":
    berechne_bild(1025, 680, 16)
    berechne_audio(44100, 16, 2, 10)

