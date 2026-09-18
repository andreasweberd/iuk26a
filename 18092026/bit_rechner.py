def berechne_bild(breite,hoehe,farbtiefe):

    bitdateigroesse = (breite*hoehe)*farbtiefe

    dateigroesse = ((bitdateigroesse / 8) / 1024) / 1024

    return dateigroesse

if __name__ == "__main__":
    
    dateigroesse = berechne_bild(1025,680,16)
    print(f"Die Dateigroesse betraegt: {dateigroesse} MiB")