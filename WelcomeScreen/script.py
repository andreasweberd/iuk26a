# URL des Github https://github.com/andreasweberd/iuk26a

def zur_schule_gehen(snack):
    print("Anziehen und losgehen ...")
    print(f"Auf dem Schulweg esse ich genüsslich {snack}!")


if __name__ == "__main__":
    print("Was für einen Snack nimmst du Heute mit?")
    essen = input()
    print("Schulmorgen beginnt.")
    mein_brot = essen
    # mein_brot = "Erdbeermarmeladenbrot mit Honig"
    zur_schule_gehen(mein_brot)
    print("In der Klasse hinsetzen")



