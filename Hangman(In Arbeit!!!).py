import random
Wörterliste = ["asdadad"]
Wort  =  random.choice(Wörterliste)
Strichliste = ["O"]


def Eingabe_überprüfung():
   Eingabe = str(input("Buchstabe eingeben:   \n"))
   if Eingabe in Wort:
        print("Richtiger Buchstabe")
        print()
        return True
    elif Eingabe == Wort:
       print("Du hast das Wort richtig erraten. Du hast gewonnen!")
       exit()   
   else:
        print("Falscher Buchstabe ein Strich kommt Dazu")
        
        return False
while Eingabe_überprüfung() == False:
    for Eingabe in Wort:
        if Eingabe_überprüfung == False:
            print(Strichliste(0 + 1))



