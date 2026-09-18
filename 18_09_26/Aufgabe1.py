
def berechne_bild(breite, hoehe, farbtiefe):
    bit = breite*hoehe*farbtiefe
    mebibyte = bit / (8 * 1024 * 1024)
    print(f"Es sind {mebibyte} Mebibytes")


if __name__ == "__main__":
    berechne_bild(1920, 1080, 24)