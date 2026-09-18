def berechne_bild(Breite, Höhe, Farbtiefe):
    Bits = Breite*Höhe*Farbtiefe
    Bytes = Bits/8
    Kibibytes = Bytes/1024
    Mebibytes = Kibibytes/1024
    return Mebibytes

def berechne_audio(Abtastrate, Bittiefe, Kanäle, Zeit_in_Sekunden):
    Bits = Abtastrate*Bittiefe*Kanäle*Zeit_in_Sekunden
    Bytes = Bits/8
    Kibibytes = Bytes/1024
    Mebibytes = Kibibytes/1024
    return Mebibytes

def berechne_video(Breite, Höhe, Farbtiefe, FPS, Abtastrate, Bittiefe, Kanäle, Zeit_in_Sekunden):
    Bild = berechne_bild(Breite, Höhe, Farbtiefe)   
    Audio = berechne_audio(Abtastrate, Bittiefe, Kanäle, Zeit_in_Sekunden)
    Video = Bild*FPS*Zeit_in_Sekunden+Audio
    Gigabyte = Video/1024
    return Gigabyte



if __name__ == "__main__":
    Bild_Bits = berechne_bild(1025,680,16)
    print("Das Bild ist " + str(Bild_Bits), "MiB groß.")

    Audio_Bits = berechne_audio(44100,16,2,10)
    print("Die Audiodatei ist " + str(Audio_Bits), "MiB groß.")

    Video_Bits = berechne_video(1920,1080,24,30,48000,16,2,60)
    print("Das Video ist " + str(Video_Bits), "GiB groß.")