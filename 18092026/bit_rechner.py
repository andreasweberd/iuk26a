def berechne_bild(breite,hoehe,farbtiefe):

    bitdateigroesse = (breite*hoehe)*farbtiefe
    dateigroesse = ((bitdateigroesse / 8) / 1024) / 1024

    return dateigroesse

def berechne_audio(abtastrate,bittiefe,kanaele,zeit_in_sekunden):

    audiobits = (abtastrate*bittiefe*kanaele*zeit_in_sekunden)
    dateigroesse = ((audiobits / 8) / 1024) / 1024

    return dateigroesse

if __name__ == "__main__":
    
    dateigroesse = berechne_audio(44100,16,2,10)
    # dateigroesse = berechne_bild(1600,680,16)
    print(f"Die Dateigroesse betraegt: {dateigroesse} MiB")