import random
import sys
import time

print("Wilkommen Bei Blackjack")
Karten = [1, 2, 3 ,4 ,5, 6 ,7 ,8 ,9 ,10 ,11]
Dealer, Dealer2, Dealer3, Spieler, Spieler2, Spieler3 = random.choice(Karten), random.choice(Karten), random.choice(Karten), random.choice(Karten), random.choice(Karten), random.choice(Karten)

while True:
   Alter = str(input("Bitte geben sie ihr Alter ein:  "))
   try:
      if Alter >= 18:
         print ("Alt genug es geht weiter")
         break
      else:
         print("Glücksspiel ist Ab 18, versuchen sie es nochmal")
   except:
      print("Bitte nächstes mal eine ganze zahl eingeben")
      sys.exit(1)

while True:
   Benutzername = str(input("Benutzer eingeben: "))
   Passwort = str(input("Passwort eingeben:  "))
   if Benutzername == "0":
      if Passwort == "0":
         print("Benutzername und Passwort Richtig")
         break
      else:
         print("Benutzername oder Passwort Falsch")
   else:
      print("Benutzername oder Passwort Falsch")

##Wieso ein string mit einem input statt einen input selber?
Spiel = str(input("Soll es Los gehen?: "))
print("\nDealers Hand")
print(Dealer + Dealer2)
print("Deine Hand")
print(Spieler + Spieler2)
Dealer5 = Dealer2 + Dealer
Spieler4 = Spieler+ Spieler2
Dealer4 = Dealer + Dealer2

if Dealer4 <= 16:
   print("Dealer muss eine Karte Ziehen!:" ) 
   print(Dealer3 + Dealer2 + Dealer)
else:
   print("Der Dealer muss nicht Ziehen!")

Dealer4 = Dealer + Dealer2 + Dealer
Nachfrage = str(input("Willst du noch eine Karte Ziehen?: (Ja/Nein) "))
while True:
   if Nachfrage == "Ja":
      print("\nDeine Hand")
      print(Spieler + Spieler2 + Spieler3)
      print("Dealers Hand")
      print(Dealer + Dealer2 + Dealer3)
      break
   else:
      print("\nDann Mal Sehen wer gewonnen Hat")
   break

Spieler = Spieler + Spieler2 + Spieler3
Dealer = Dealer + Dealer2 + Dealer3

print("Ergebnis wird geladen")
time.sleep(3)

print("\nSpieler:", Spieler, "\nDealer", Dealer)
if Dealer >= 22:
   print("Dealer hat überschritten, Du hast Gewonnen!")
elif Spieler >= 22:
   print("Du hast überschritten, Der  Dealer hat gewonnen!")
elif Dealer < Spieler & Spieler <=21:
   print("Du hast Gewonnen!")
elif Spieler < Dealer & Dealer <=21:
   print("Dealer Gewinnt")
elif Spieler == Dealer:
   print("unentschieden")
else:
   print("error")

sys.exit(1)