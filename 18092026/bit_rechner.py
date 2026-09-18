def berechne_bild(breite,hoehe,farbtiefe):

    bitdateigroesse = (breite*hoehe)*farbtiefe
    dateigroesse_bild = ((bitdateigroesse / 8) / 1024) / 1024

    return dateigroesse_bild

def berechne_audio(abtastrate,bittiefe,kanaele,zeit_in_sekunden):

    audiobits = (abtastrate*bittiefe*kanaele*zeit_in_sekunden)
    dateigroesse_audio = ((audiobits / 8) / 1024) / 1024

    return dateigroesse_audio

def berechne_video(breite,hoehe,farbtiefe,fps,abtastrate,bittiefe,kanaele,zeit_in_sekunden):

    dateigroesse_bild = berechne_bild(breite,hoehe,farbtiefe)
    dateigroesse_audio = berechne_audio(abtastrate,bittiefe,kanaele,zeit_in_sekunden)

    dateigroesse_video = (dateigroesse_bild * fps * zeit_in_sekunden) + dateigroesse_audio

    return dateigroesse_video


if __name__ == "__main__":
    
    dateigroesse_audio = berechne_audio(44100,16,2,10)
    dateigroesse_bild = berechne_bild(1600,680,16)

    print(f"Die Dateigroesse des Bildes betraegt: {dateigroesse_bild} MiB")
    print(f"Die Dateigroesse der Audio betraegt: {dateigroesse_audio} MiB")

    dateigroesse_video = berechne_video (1920,1080,24,30,48000,16,2,60)
    print(f"Die Dateigroesse des Videos betraegt: {dateigroesse_video} MiB")