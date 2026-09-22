def berchene_bild(breite, hoehe, farbtiefe):
    Bits = breite * hoehe * farbtiefe
    Bytes = Bits / 8
    Kibibytes = Bytes / 1024
    Mebibytes = Kibibytes / 1024
    return Mebibytes

def berechne_audio(abtastrate, bittiefe, kaneale, zeit_in_sekunden):
    abtastrate = 44100
    bittiefe = 16
    kaneale = 2
    zeit_in_sekunden = 10
    Audio_Bits = abtastrate * bittiefe * kaneale * zeit_in_sekunden
    Audio_Bytes = Audio_Bits / 8
    Audio_Kibibytes = Audio_Bytes / 1024
    Audio_Mebibytes = Audio_Kibibytes / 1024
    Audio_Gigibytes = Audio_Mebibytes / 1024
    return Audio_Gigibytes

def berechne_Video(breite, hoehe, farbtiefe, fps, abtastrate, bittiefe, kaneale, zeit_in_sekunden,):
    Gesamt_Bild =  berchene_bild(breite, hoehe, farbtiefe) * fps * zeit_in_sekunden

    Gesamt_Audio = berechne_audio(abtastrate, bittiefe, kaneale, zeit_in_sekunden)

    return Gesamt_Audio + Gesamt_Bild /1024

if __name__ == "__main__":
    Ergebnis = berchene_bild(1025,680,16)
    Audio_bits = berechne_audio(44100, 16, 2,10)
    Gesamt_Video = berechne_Video(1920, 1080, 24, 30, 48000, 16, 2, 60)
    print("Das Ergebnis ist: " + str(Ergebnis))
    print("Das Ergebnis der Audio ist: " + str(Audio_bits))
    print("Das 1 minütige Full-HD Video hat: " + str(Gesamt_Video))




