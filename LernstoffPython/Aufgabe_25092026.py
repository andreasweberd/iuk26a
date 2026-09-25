if __name__ == "__main__":
   liter = float(input("Wie viele Liter hast du getankt?\n"))
   kmh = float(input("Wie viele kmh bist du gefahren?\n"))
   verbrauch = liter / kmh * 100

if verbrauch < 8:
      print("Sparsam")
else: print("nicht sparsam")

