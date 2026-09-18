def berechne_bild(breite,hoehe,farbtiefe):
    Bits = breite*hoehe*farbtiefe
    Bytes = Bits/8
    Kibibytes = Bytes/1024
    Mebibytes = Kibibytes/1024
    return Mebibytes

def berechne_audio(abtastrate,bittiefe,kanaele,zeit_in_sekunden):
    AudioBits = abtastrate*bittiefe*kanaele*zeit_in_sekunden
    AudioBytes = AudioBits/8
    AudioKibibytes = AudioBytes/1024
    AudioMebibytes = AudioKibibytes/1024
    return AudioMebibytes

def berechne_video(breite,hoehe,farbtiefe,fps,abtastrate,bittiefe,kanaele,zeit_in_sekunden):
    AudioData = berechne_audio(abtastrate,bittiefe,kanaele,zeit_in_sekunden)
    FrameData = berechne_bild(breite,hoehe,farbtiefe)
    VideoData = FrameData*fps*zeit_in_sekunden
    return VideoData+AudioData

if __name__ == "__main__":
    Ergebnis = berechne_bild(1025,680,16)
    print("Das Bildergebnis ist: " + str(Ergebnis) + " MiB")
    AudioErgebnis = berechne_audio(44100,16,2,10)
    print("Das Audioergebnis ist: " + str(AudioErgebnis) + " MiB")
    VideoErgebnis = berechne_video(1920,1080,24,30,48000,16,2,60)
    print("Das Videoergebnis ist: " + str(VideoErgebnis) + " MiB")
