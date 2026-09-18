def berechne_bild(breite, höhe, farbtiefe):

    Dateigröße = breite * höhe * farbtiefe 
    Bytes = Dateigröße/8 
    Kibibytes = Bytes/1024
    Mebibytes = Kibibytes/1024
    return Mebibytes

def berechne_audio(abtastrate, bittiefe, kanäle, zeit_in_sekunden):

    Audiobits = abtastrate * bittiefe * kanäle * zeit_in_sekunden 
    bytes = Audiobits / 8
    Mebibytes = bytes/1024/1024
    return Mebibytes

if __name__ == '__main__':

    breite = 1025 
    höhe = 680
    farbtiefe = 16

    Ergebniss = berechne_bild(breite, höhe, farbtiefe)
    print('Das Ergebnis ist: ' + str(Ergebniss))
    
    abtastrate = 44100
    bittiefe = 16
    kanäle = 2
    zeit_in_sekunden = 10
    

    Ergebniss = berechne_audio(abtastrate, bittiefe, kanäle, zeit_in_sekunden)

    print('Das Ergebnis ist: ' + str(Ergebniss))
    


