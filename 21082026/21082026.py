
#Funktionsdefinition (wartet nur, noch keine Ausfuehrung)
def gehe_zur_schule(snack):   #"snack" ist der Parameter
    print("Anziehen und losgehen")
    print(f"Auf dem Schulweg esse ich: {snack}")


#Einsprungpunkt (Ab hier startet das Programm)
if __name__ == "__main__":
    print("Schulmorgn beginnt.")

    mein_brot = "Kaesebrot"
    gehe_zur_schule(mein_brot) #Parameter wird ersetzt durch etwas, bzw. wird aufgerufen mit Parameter

    print("In der Klasse hinsetzen.") 

