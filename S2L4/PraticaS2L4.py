print("Il programma calcola il perimetro di una figura geometrica scelta dall'utente")
print("1. Quadrato")
print("2. Rettangolo")
print("3. Cerchio")
sce = input("Scegli: ")

if(sce == "1"):
    print("Hai scelto quadrato!")
    lato = float(input("Inserisci la lughezza del lato: "))
    print(f"Il quadrato con lato {lato} ha perimetro {lato*4}")
elif(sce == "2"):
    print("Hai scelto rettangolo!")
    base = float(input("Inserisci la lughezza della base: "))
    altezza = float(input("Inserisci l'altezza: "))
    print(f"Il rettangolo con base {base} ed altezza {altezza} ha perimetro {(base*2)+(altezza*2)}")
elif(sce == "3"):
    print("Hai scelto cerchio!")
    raggio = float(input("Inserisci la lughezza del raggio: "))
    print(f"Il cerchio con raggio {raggio} ha perimetro {2*3.14*raggio}")
else:
    print("Inserisci un numero da 1 a 3!")