def kaufen (artikel, preis,anzahl):
    gesamt_preis= preis * anzahl
    print(f"ich kaufe {anzahl}x {artikel} für insgesamt {gesamt_preis} euro.")


if __name__ == "__main__":
    kaufen("Apfel", 3, 2)