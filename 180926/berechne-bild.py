def berechne_bild(breite, hoehe, farbtiefe):
    Bits = breite * hoehe * farbtiefe
    Bytes = Bits / 8
    Kibibytes = Bytes / 1024
    Mebibytes = Kibibytes / 1024
    return Mebibytes


def berechne_audio(abtastrate, bittiefe, kanalae, zeit_in_sekunden):
    Bits = abtastrate * bittiefe * kanalae * zeit_in_sekunden
    Bytes = Bits / 8
    Kibibytes = Bytes / 1024
    Mebibytes = Kibibytes / 1024
    return Mebibytes



if __name__ == "__main__":
    Ergebnis = berechne_bild(1025, 680, 16)
    print("Das Ergebnis ist:" + str(Ergebnis))

    Audio_Bits = berechne_audio(44100, 16, 2, 10)
    print("Die Audiodatei ist:" + str(Audio_Bits))

def berechne_video(bild_meB,audio_meB, fps, zeit_in_sekunden):
    mebibyte = bild_meB * fps * zeit_in_sekunden + audio_meB
    return(mebibyte)

if __name__ == "__main__":
    video_miB = (berechne_video(berechne_bild(1920, 1080, 24), berechne_audio(48000, 16, 2, 60), 30, 60))
    video_Gib=video_miB /1024
    print(f"Die Größe des Videos b-eträgt: {video_miB:.2f} MiB")