def berechne_bild(breite, höhe, farbtiefe):

    Dateigröße = breite * höhe * farbtiefe 
    Bytes = Dateigröße / 8 
    Kibibytes = Bytes / 1024
    Mebibytes = Kibibytes / 1024
    return Mebibytes

def berechne_audio(abtastrate, bittiefe, kanäle, zeit_in_sekunden):

    Audiobits = abtastrate * bittiefe * kanäle * zeit_in_sekunden 
    bytes = Audiobits / 8
    Mebibytes = bytes / 1024 / 1024
    return Mebibytes

def berechne_video(breite, höhe, farbtiefe, FPS, abtastrate, bittiefe, kanäle, zeit_in_sekunden):

    Ergebniss_bild = berechne_bild(breite, höhe,farbtiefe)
    Ergebniss_audio = berechne_audio(abtastrate, bittiefe, kanäle, zeit_in_sekunden)


    Bildbits = Ergebniss_bild * FPS * zeit_in_sekunden
    ergebniss_video = Bildbits + Ergebniss_audio

    return ergebniss_video

if __name__ == '__main__':

    breite = 1025 
    höhe = 680
    farbtiefe = 16
    Ergebniss_video = berechne_video(1920, 1080, 24, 30, 48000, 16, 2, 60)

    Ergebniss_bild = berechne_bild(breite, höhe, farbtiefe)
    print('Das Ergebnis vom Bild ist: ' + str(Ergebniss_bild))

    abtastrate = 44100
    bittiefe = 16
    kanäle = 2
    zeit_in_sekunden = 10

    print(f'Ergebnis Video: {Ergebniss_video}')
    

    Ergebniss_audio = berechne_audio(abtastrate, bittiefe, kanäle, zeit_in_sekunden)

    print('Das Ergebnis der Audio ist: ' + str(Ergebniss_audio))


