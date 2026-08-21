def SahurStrafe():
    schaedel = r"""
      ______
   .-        -.
  /            \
 |,  .-.  .-.  ,|
 | )(_ /  \ _)( |
 |/     /\     \|
 (_     ^^     _)
  \__|IIIIII|__/
    """
    print(schaedel)

A = "3"
if __name__ == "__main__":
    print("Sahur?")

    A = input("Wie viele Tungs?\n")

if A != "3":
    print("FALSCH!!")
    SahurStrafe()
else:
    print("Sahur.")
