prices = {1: 2.50, 2: 3.00, 3: 2.00}
inventar = {1: 10, 2: 5, 3: 7}
product_id = 3
lagerbestand = 7

def process_client_order(product_id):
    lagerbestand = inventar[product_id]

    if lagerbestand == 0:
        print('ERROR')
        return                                  #Damit wird das immer wiederholt solange dre Lagerbestnad == 0 ist 

    preis = prices[product_id]
    einwurf = 0

    print('Preis' + str(preis) + '€')


    while einwurf < preis:
        münze = float(input('Bitte Münze einwerfen: '))

        if münze >= 0.10 and münze <= 2.00:
            einwurf = einwurf + münze

    abbruch = input('Abbruch')

    if abbruch == 'ja':
        return
    print('Hier ist ihr Getränk')

    inventar[product_id] = lagerbestand - 1
    print('Hier ist ihr Rückgeld: ' + str(einwurf - preis) + '€')
    return 

if __name__ == '__main__':
    process_client_order(2)