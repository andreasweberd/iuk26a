def berechne_bild(breite, hoehe, farbtiefe):

    dateigröße = breite * hoehe * farbtiefe

    dateigröße = dateigröße / 8
    dateigröße = dateigröße / 1024
    dateigröße = dateigröße / 1024

    print(f"Das Ergebnis ist {dateigröße} MiB")

def berechne_audio(abtastrate, bittiefe, kanaele, zeit_in_sekunden):


    audio_bits = abtastrate * bittiefe * kanaele * zeit_in_sekunden

    audio_bits = audio_bits / 8
    audio_bits = audio_bits / 1024
    audio_bits = audio_bits / 1024

    print(f"Das Ergebnis ist {audio_bits} MiB")

def berechne_video(breite, hoehe, farbtiefe, fps, abtastrate, bittiefe, kanaele, zeit_in_sekunden):

    bild_bits = breite * hoehe * farbtiefe * fps * zeit_in_sekunden
    bild_bits = bild_bits + abtastrate * bittiefe * kanaele * zeit_in_sekunden


    bild_bits = bild_bits / 8
    bild_bits = bild_bits / 1024
    bild_bits = bild_bits / 1024
    bild_bits = bild_bits / 1024

    print(f"Das gesamte Video ist: {bild_bits} groß")

if __name__ == "__main__":

    breite = 1025
    hoehe = 680
    farbtiefe = 16

    berechne_bild(breite, hoehe, farbtiefe)

    abtastrate = 44100
    bittiefe = 16
    kanaele = 2
    zeit_in_sekunden = 10

    berechne_audio(abtastrate, bittiefe, kanaele, zeit_in_sekunden)

    breite = 48000
    hoehe = 16
    farbtiefe = 24
    fps = 60
    abtastrate = 4800
    bittiefe = 16
    kanaele = 2
    zeit_in_sekunden = 60

    berechne_video(breite, hoehe,farbtiefe,fps,abtastrate,bittiefe,kanaele,zeit_in_sekunden)
