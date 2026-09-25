def gefahrene_km():
    km = float(input('Wieviel Km bist du gefahren? '))
    print('Du bist ' + str(km) + ' km gefahren')

    liter = float(input('Wieviel Liter hast du verbraucht? '))
    print('Du hast ' + str(liter) + ' Liter verbraucht')
   
    verbrauch = (liter / km) * 100
    print('Dein Verbrauch liegt bei: ' + str(verbrauch) + ' Liter auf 100 km')
    
   
    return verbrauch


mein_verbrauch = gefahrene_km()


if mein_verbrauch < 8:
    print('Sparsam')
else:
    print('Nicht Sparsam')