# --- FUNKTIONSDEFINITION (Wartet nur, wird noch NICHT ausgeführt!) ---
def gehe_zur_schule(snack):
    print("Anziehen und losgehen...")
    print(f"Auf dem Schulweg esse ich: {snack}")


# --- EINSPRUNGPUNKT (Hier startet das Programm wirklich!) ---
if __name__ == "__main__":
    print("Schulmorgen beginnt.")

    mein_brot = "Käsebrot"
    gehe_zur_schule(mein_brot)  # Funktionsaufruf mit Parameter

    print("In der Klasse hinsetzen.")