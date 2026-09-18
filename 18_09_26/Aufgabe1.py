def berechne_bild(breite, hoehe, farbtife):
    bild_Bit = breite * hoehe * farbtife
    bild_Mebibyte = bild_Bit / (8 * 1024 * 1024)
    return bild_Mebibyte

def berechne_audio (abtastrate, bittiefe, kanaele, zeit):
    audio_Bit = abtastrate * bittiefe * kanaele * zeit
    audio_Mebibyte = audio_Bit / (8 * 1024 * 1024)
    return audio_Mebibyte

def berechne_video (breite, hoehe, farbtife, fps, abtastrate, bittiefe, kanaele, zeit):
    bild = berechne_bild(breite, hoehe, farbtife)
    video = bild * fps * zeit
    audio = berechne_audio (abtastrate, bittiefe, kanaele, zeit)
    video_mit_ton = audio + video
    return video_mit_ton


if __name__ == "__main__":
    ergebnis = berechne_video(1920, 1080,24,30, 48000, 16,2,60)
    print(f"die Dateigröße video mit ton beträgt {ergebnis} Mebibyte")
    gibibyte = ergebnis / 1024
    print (f"die Dateigröße video mit ton beträgt {gibibyte} Gibibyte")