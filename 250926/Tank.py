if __name__=="__main__":
    liter= float(input("wie viele liter sind im tank"))
    km= float(input("wie viele km bist du gefahren"))
    verbrauch= liter / km * 100

if verbrauch > 8:
    print ("nicht sparsam")
else:
    print("sparsam")


