def berechne_bild(breite, hoehe, farbtife):
    dateigroeße_Bit = breite * hoehe * farbtife
    dateigroeße_Mebibyte = dateigroeße_Bit / (8 * 1024 * 1024)
    print(f"die Dateigröße beträgt {dateigroeße_Mebibyte} Mebibyte")

def berechne_audio (abtastrate, bittiefe, kanaele, zeit):
    audio_Bit = abtastrate * bittiefe * kanaele * zeit
    audio_Mebibyte = audio_Bit / (8 * 1024 * 1024)
    return audio_Mebibyte

if __name__ == "__main__":
    bild = berechne_bild(1025, 680, 16)
    audio = berechne_audio(44100,16,2,10)

    print(f"die Dateigröße Audio beträgt {audio} Mebibyte")