def berechne_bild(breite,hoehe,farbtiefe):
    Bits = breite*hoehe*farbtiefe
    Bytes = Bits/8
    Kibibytes = Bytes/1024
    Mebibytes = Kibibytes/1024
    return Mebibytes

if __name__ == "__main__":
    Ergebnis = berechne_bild(1025,680,16)
    print("Das Ergebnis ist: " + str(Ergebnis))
# Pixelanzahl: 1025 × 680 = 697.000 Pixel
# Bits: 697.000 × 16 = 11.152.000 Bits
# Bytes: 11.152.000 / 8 = 1.394.000 Bytes
# Kibibytes (KiB): 1.394.000 / 1024 = 1.361,328125 KiB
# Mebibytes (MiB): 1.361,328125 / 1024 = ~1,33 MiB
