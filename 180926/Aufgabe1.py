def berechne_bild(breite,hoehe,farbtiefe):
    Bits = breite*hoehe*farbtiefe
    Bytes = Bits/8
    Kibibytes = Bytes/1024
    Mebibytes = Kibibytes/1024
    return Mebibytes

if __name__=="__main__":
    Ergebnis = berechne_bild(1025,680,16)
    print(f"Das Ergebnis ist: " + str(Ergebnis))


def berechne_audio(abtastrate,bittiefe,kanaele,zeit_in_sekunden):
    bits = abtastrate*bittiefe*kanaele*zeit_in_sekunden
    bytes = bits/8
    return bytes/1024/1024


if __name__=="__main__":
    Ergebnis = berechne_audio(44100,16,2,10)
    print(f"Das Ergebnis ist: {Ergebnis}")




def berechne_video(breite,hoehe,farbtiefe,fps,abtastrate,bittiefe,kanaele,zeit_in_sekunden):
    bits = ((berechne_bild(breite,hoehe,farbtiefe)*fps*zeit_in_sekunden)+berechne_audio(abtastrate,bittiefe,kanaele,zeit_in_sekunden))
    bytes = bits/8
    return (bytes/1024/1024)/1024

if __name__=="__main__":
    Ergebnis= berechne_video(1920,1080,24,30,48000,16,2,60)
    print(f" Das Video hat benötigt {Ergebnis} Speicherplatz")




    
