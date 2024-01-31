##Random Placeholder Text for Pylint to be happy
import random
import sys
import time

print("Wilkommen Bei Blackjack")
Karten = [1, 2, 3 ,4 ,5, 6 ,7 ,8 ,9 ,10 ,11]
Dealer1, Dealer2, Dealer3, Spieler1, Spieler2, Spieler3 = random.choice(Karten), random.choice(Karten), random.choice(Karten), random.choice(Karten), random.choice(Karten), random.choice(Karten)

SpielerEnd = 0
DealerEnd = 0

while True:
    ALTER = str(input("Bitte geben sie ihr Alter ein:  "))
    try:
        if eval(ALTER) >= 18:
            print ("Alt genug es geht weiter")
            break
        else:
            print("Glücksspiel ist Ab 18, versuchen sie es nochmal")
    except:
        print("Bitte nächstes mal eine ganze zahl eingeben")
        sys.exit(1)
""""
while True:
    BENUTZERNAME = str(input("Benutzer eingeben: "))
    PASSWORT = str(input("Passwort eingeben:  "))
    if BENUTZERNAME == "0":
        if PASSWORT == "0":
            print("Benutzername und Passwort Richtig")
            break
        else:
            print("Benutzername oder Passwort Falsch")
    else:
        print("Benutzername oder Passwort Falsch")
"""


input("Soll es Los gehen?: ")
##First Cards
print("\nDeine Hand")
SpielerEnd = SpielerEnd + Spieler1
print(SpielerEnd)
print("Dealers Hand")
DealerEnd = DealerEnd + Dealer1
print(DealerEnd)
##Second Cards
print("\nDeine Hand")
SpielerEnd = SpielerEnd + Spieler2
print(Spieler1, "+", Spieler2)
print("Dealers Hand")
print(DealerEnd, "+", "?")
DealerEnd = DealerEnd + Dealer2

NACHFRAGE = str(input("Willst du noch eine Karte Ziehen?: (Ja/Nein) "))
while True:
    if NACHFRAGE == "Ja":
        print("\nDeine Hand")
        print(Spieler1, "+", Spieler2, "+", Spieler3)
        SpielerEnd = SpielerEnd + Spieler3
        print("Dealers Hand")
        print(Dealer1, "+", "?")
        break
    else:
        print("\nDann Mal Sehen wer gewonnen Hat")
        break

print("Dealer zeigt seine Karten")
time.sleep(3)

print("\nSpieler:", SpielerEnd, "\nDealer", DealerEnd)
if DealerEnd >= 22:
    print("Dealer hat überschritten, Du hast Gewonnen!")
elif SpielerEnd >= 22:
    print("Du hast überschritten, Der  Dealer hat gewonnen!")
elif DealerEnd < SpielerEnd & SpielerEnd <=21:
    print("Du hast Gewonnen!")
elif SpielerEnd < DealerEnd & DealerEnd <=21:
    print("Dealer Gewinnt")
elif SpielerEnd == DealerEnd:
    print("unentschieden")
else:
    print("error")

sys.exit(1)
