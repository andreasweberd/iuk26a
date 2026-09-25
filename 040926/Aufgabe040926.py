def zur_schule_gehen(snack):
    print("anziegen und losgehen...")
    print(f"Auf dem Schulweg esse ich genüsslich [{snack}!")

if __name__=="__main__":
    print("Was für einen Snack nimmst du heute mit?")
    essen = input()
    print("Schulmorgen beginnt.")
    mein_brot = essen
    # mein_brot = " Erdbeermarmeladenbrot mit Honig"
    zur_schule_gehen(mein_brot)
    print("in der Klasse hinsetzen")

