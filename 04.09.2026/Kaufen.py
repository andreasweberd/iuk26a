def kaufen(artikel, Preis, Anzahl):
    
    gesamtpreis = Preis * Anzahl
    
    print(f'Ich Kaufe {Anzahl} {artikel} für insgesamt {gesamtpreis}')

# Hiermit fängt das Programm an 
if __name__ == '__main__':
    
    print('Ich gehe in den Supermarkt')
    print()

    artikel = 'Brot'  
    anzahl = 3  
    preis = 1.50  

    # Ruft die Kauf funktion auf
    kaufen(artikel, preis, anzahl)
