import random
##Used for choosing given numbers randomly for the hand cards
import sys
##Used as replacement for exit with sys.exit(1)
import time
##Used for sleep

print("Wilkommen Bei Blackjack")
Karten = [1, 2, 3 ,4 ,5, 6 ,7 ,8 ,9 ,10 ,11]
Dealer1, Dealer2, Dealer3 = random.choice(Karten), random.choice(Karten), random.choice(Karten)
Spieler1, Spieler2, Spieler3 = random.choice(Karten), random.choice(Karten), random.choice(Karten)

SPIELEREND = 0
DEALEREND = 0

while True:
    ##Security question that wont let you go further if you are under 18
    ALTER = str(input("Bitte geben sie ihr Alter ein:  "))
    try:
        if eval(ALTER) >= 18:
            print ("Alt genug es geht weiter")
            break
        print("Glücksspiel ist Ab 18, versuchen sie es nochmal")
    except:
        print("Bitte nächstes mal eine ganze zahl eingeben")
        sys.exit(1)

while True:
    BENUTZERNAME = str(input("Benutzer eingeben: "))
    PASSWORT = str(input("Passwort eingeben:  "))
    if BENUTZERNAME == "0":
        if PASSWORT == "0":
            print("Benutzername und Passwort Richtig")
            break
        print("Benutzername oder Passwort Falsch")
    print("Benutzername oder Passwort Falsch")



input("Soll es Los gehen?: ")
##First Cards
print("\nDeine Hand")
SPIELEREND = SPIELEREND + Spieler1
print(SPIELEREND)
print("Dealers Hand")
DEALEREND = DEALEREND + Dealer1
print(DEALEREND)
##Second Cards
print("\nDeine Hand")
SPIELEREND = SPIELEREND + Spieler2
print(Spieler1, "+", Spieler2)
print("Dealers Hand")
print(DEALEREND, "+", "?")
DEALEREND = DEALEREND + Dealer2
NACHFRAGE = str(input("Willst du noch eine Karte Ziehen?: (Ja/Nein) "))
while True:
    ##Adds another card to both Player and Dealer if you write yes (change this in future)
    if NACHFRAGE in ('Ja', 'ja'):
        print("\nDeine Hand")
        print(Spieler1, "+", Spieler2, "+", Spieler3)
        SPIELEREND = SPIELEREND + Spieler3
        print("Dealers Hand")
        print(Dealer1, "+", "?")
        break
    print("\nDann Mal Sehen wer gewonnen Hat")
    break

print("Dealer zeigt seine Karten")
time.sleep(3)

print("\nSpieler:", SPIELEREND, "\nDealer", DEALEREND)
if DEALEREND >= 22:
    print("Dealer hat überschritten, Du hast Gewonnen!")
elif SPIELEREND >= 22:
    print("Du hast überschritten, Der  Dealer hat gewonnen!")
elif DEALEREND < SPIELEREND & SPIELEREND <=21:
    print("Du hast Gewonnen!")
elif SPIELEREND < DEALEREND & DEALEREND <=21:
    print("Dealer Gewinnt")
elif SPIELEREND == DEALEREND:
    print("unentschieden")
else:
    print("error")

sys.exit(1)
