
import random

Waffen = [
    "Schwert",
    "Langschwert",
    "Speer",
    "Fäuste",
    "Hellebarde",
    "Flegel"
]

WeaponStats = {
    "Schwert": {
        "Damage": 25,
        "Accuracy": 50
    },
    "Langschwert": {
        "Damage": 40,
        "Accuracy": 40
    },
    "Speer": {
        "Damage": 20,
        "Accuracy": 70
    },
    "Fäuste": {
        "Damage": 10,
        "Accuracy": 90
    },
    "Hellebarde": {
        "Damage": 30,
        "Accuracy": 60
    },
    "Flegel": {
        "Damage": 60,
        "Accuracy": 30
    }
}

Waffe = "Fäuste"

PlayerHealth = 100
SahurHealth = 300

def PrintHealth():
    print("\n---------------------------")
    print(f"Dein HP: {PlayerHealth}")
    print(f"Sahur HP: {SahurHealth}")
    print("---------------------------")


def GameOver():
    print("\nSahur hat dich getötet.")
    print("GAME OVER")


def GameWin():
    print("\nSahur ist tot.")
    print("DU HAST GEWONNEN!")

def Attack(Damage, Accuracy):
    Roll = random.randint(1, 100)

    # Trefferchance zwischen 0 und 100 halten
    Accuracy = max(0, min(100, Accuracy))

    print(f"Trefferchance: {Accuracy}%")
    print(f"Gewürfelt: {Roll}")

    if Roll <= Accuracy:
        print(f"GETROFFEN! Sahur nimmt {Damage:.1f} Schaden.")
        return Damage

    else:
        print("NICHT GETROFFEN!")
        return 0


def SahurTurn():
    global PlayerHealth

    print("\nSAHUR GREIFT AN!")

    Damage = 40
    Accuracy = 30

    DamageDealt = Attack(Damage, Accuracy)

    # Sahur macht Schaden am Spieler
    if DamageDealt > 0:
        print(f"Du nimmst {DamageDealt:.1f} Schaden.")

    PlayerHealth -= DamageDealt

def PlayerTurn(Choice):
    global PlayerHealth
    global SahurHealth

    if Choice == "1":
        Damage = WeaponStats[Waffe]["Damage"]
        Accuracy = WeaponStats[Waffe]["Accuracy"]

        print("\nANGRIFF!")

        DamageDealt = Attack(Damage, Accuracy)
        SahurHealth -= DamageDealt

    elif Choice == "2":
        Damage = WeaponStats[Waffe]["Damage"] * 0.8
        Accuracy = WeaponStats[Waffe]["Accuracy"] * 1.2

        print("\nLEICHTER ANGRIFF!")

        DamageDealt = Attack(Damage, Accuracy)
        SahurHealth -= DamageDealt

    elif Choice == "3":
        Damage = WeaponStats[Waffe]["Damage"] * 1.2
        Accuracy = WeaponStats[Waffe]["Accuracy"] * 0.8

        print("\nSCHWERER ANGRIFF!")

        DamageDealt = Attack(Damage, Accuracy)
        SahurHealth -= DamageDealt

    elif Choice == "4":
        PlayerHealth += 10

        if PlayerHealth > 100:
            PlayerHealth = 100

        print("\n10 HP geheilt.")

    else:
        print("\nUngültige Aktion!")

def WeaponSelection():
    global Waffe

    print("Welche Waffe wählst du?\n")

    for Nummer, WaffeName in enumerate(Waffen, start=1):
        Damage = WeaponStats[WaffeName]["Damage"]
        Accuracy = WeaponStats[WaffeName]["Accuracy"]

        print(
            f"{Nummer}. {WaffeName} "
            f"| Schaden: {Damage} "
            f"| Trefferchance: {Accuracy}%"
        )

    while True:
        try:
            Waffenwahl = int(input("\nWAHL: "))

            if 1 <= Waffenwahl <= len(Waffen):
                Waffe = Waffen[Waffenwahl - 1]
                break

            print("Falsche Zahl.")

        except ValueError:
            print("Falsche Zahl.")

    print(f"\nDeine Waffe ist: {Waffe}")
    
def SahurKampf():
    global PlayerHealth
    global SahurHealth

    Turn = "Player"

    while PlayerHealth > 0 and SahurHealth > 0:

        PrintHealth()

        if Turn == "Player":
            print(
                "\nWas tust du?\n"
                "1. Angriff\n"
                "2. Leichter Angriff\n"
                "3. Schwerer Angriff\n"
                "4. Heilen"
            )

            Choice = input("\nWAHL: ")

            PlayerTurn(Choice)

            if SahurHealth <= 0:
                break

            Turn = "Sahur"

        elif Turn == "Sahur":
            SahurTurn()

            if PlayerHealth <= 0:
                break

            Turn = "Player"

    if PlayerHealth <= 0:
        GameOver()

    elif SahurHealth <= 0:
        GameWin()

if __name__ == "__main__":

    print("Tung Tung Tung Sahur kommt.\n")

    WeaponSelection()

    print("\n---------------------------")
    print("\nTUNG TUNG TUNG SAHUR erscheint.")

    SahurKampf()
