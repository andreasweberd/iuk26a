# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def berechne_bild(breite, hoehe, farbtiefe):
    # Use a breakpoint in the code line below to debug your script.
    Bits = breite*hoehe*farbtiefe
    Bytes = Bits/8
    Kibibytes = Bytes/1024
    Mebibytes = Kibibytes/1024
    return Mebibytes

def berechne_audio(Abtastrate, Bittiefe, Kanaele, Zeit_in_sekunden):
    Audiobits = Abtastrate*Bittiefe*Kanaele*Zeit_in_sekunden
    Audiobytes = Audiobits/8
    Audiokibibytes = Audiobytes/1024
    Audiomebibytes = Audiokibibytes/1024
    return Audiomebibytes

def berechne_video(breite,hoehe,farbtiefe,fps,abtastrate,bittiefe,kanaele,zeit_in_sekunden):
    Audio = berechne_audio(abtastrate,bittiefe,kanaele,zeit_in_sekunden)
    Bild = berechne_bild(breite,hoehe,farbtiefe)
    Video =  (Bild * fps * zeit_in_sekunden + Audio)/1024
    return Video


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    Ergebnis = berechne_bild(1025,680,16)
    print('Das Ergbnis 1 ist:'  + str(Ergebnis))

    Ergebnis2 = berechne_audio(44100,16,2,10)
    print('Das Ergbnis 2 ist:' + str(Ergebnis2))

    Ergebnis3 = berechne_video(1920, 1080, 24, 30, 48000, 16, 2, 60)
    print('Das Ergbnis 3 ist:' + str(Ergebnis3))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
