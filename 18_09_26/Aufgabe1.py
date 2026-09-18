def berechne_bild(breite, hoehe, farbtife):
    dateigroeße_Bit = breite * hoehe * farbtife
    dateigroeße_Mebibyte = dateigroeße_Bit / (8 * 1024 * 1024)
    print(f"die Dateigröße beträgt {dateigroeße_Mebibyte} Mebibyte")

if __name__ == "__main__":
    berechne_bild(1025, 680, 16)