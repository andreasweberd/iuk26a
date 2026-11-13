def ueberwachung(temp):
    limit = 85
    while temp <= 90:
        temp = temp + 2
        if temp >= limit:
            print("WARNUNG:Zu heiß")
        elif temp <= limit:
            print("Temperatur: OK")

    else:
        return "Notabschaltung"

print(ueberwachung(0))
