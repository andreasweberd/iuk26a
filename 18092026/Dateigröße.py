#Funktion Aufgabe 1
def berechne_bild(breite, hoehe, farbtiefe):
    bild_bits = breite * hoehe * farbtiefe
    bild_MiB = bild_bits / 8 / 1024 / 1024
    print(f"Die Bildgröße beträgt {bild_MiB} MiB.")
    return bild_bits

#Funktion Aufgabe 2
def berechne_audio(abtastrate, bittiefe, kanaele, zeit_in_sekunden):
    audio_bits = abtastrate * bittiefe * kanaele * zeit_in_sekunden
    audio_MiB = audio_bits / 8 / 1024 / 1024
    print(f"Die Audiogröße beträgt {audio_MiB} MiB.")
    return audio_bits

#Funktion Aufgabe 3
def berechne_video(breite, hoehe, farbtiefe, fps, abtastrate, bittiefe, kanaele, zeit_in_sekunden):
    videospur_bits = berechne_bild(breite, hoehe, farbtiefe) * fps * zeit_in_sekunden
    audiospur_bits = berechne_audio(abtastrate, bittiefe, kanaele, zeit_in_sekunden)
    video_bits = videospur_bits + audiospur_bits
    video_GiB = video_bits / 8 / 1024 / 1024 / 1024
    print(f"Die Videogröße beträgt {video_GiB} GiB.")

if __name__ == "__main__":
    berechne_video(1920, 1080, 24, 30, 48000, 16, 2, 60)
