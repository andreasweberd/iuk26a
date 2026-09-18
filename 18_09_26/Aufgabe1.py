
def berechne_bild(breite, hoehe, farbtiefe):
    bit = breite*hoehe*farbtiefe
    mebibyte = bit / (8 * 1024 * 1024)
    return(mebibyte)

def berechne_audio(abtastrate, bittiefe, kanaele, zeit_in_sekunden):
    bit = abtastrate * bittiefe * kanaele * zeit_in_sekunden
    mebibyte = bit / (8 * 1024 * 1024)
    return(mebibyte)

def berechne_video(bild_meB,audio_meB, fps, zeit_in_sekunden):
    mebibyte = bild_meB * fps * zeit_in_sekunden + audio_meB
    return(mebibyte)

if __name__ == "__main__":
    video_miB = (berechne_video(berechne_bild(1920, 1080, 24), berechne_audio(48000, 16, 2, 60), 30, 60))
    print(f"Die Größe des Videos beträgt: {video_miB:.2f} MiB")

