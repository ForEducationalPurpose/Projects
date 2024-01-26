import random
print("Wilkommen Bei Blackjack")
Karten = [1, 2, 3 ,4 ,5, 6 ,7 ,8 ,9 ,10 ,11, ]
Dealer, Dealer2, Dealer3, Spieler, Spieler2, Spieler3 = random.choice(Karten), random.choice(Karten), random.choice(Karten), random.choice(Karten), random.choice(Karten), random.choice(Karten)
Alter = int(input(("Glücksspiel ist Ab 18. Bitte geben sie ihr Alter ein:  ")))
if Alter < 18:
    print("zu Jung komm wieder wenn du alt genug bist ")
   exit()
else:
   print ("Alt genug es geht weiter")

Benutzername = str(input("Benutzer eingeben: "))
Passwort = int(input("Passwort eingeben:  "))

if Benutzername == ".":
   print("Benutzer Richtig")
else:
   print("Falsch")
   exit()

if Passwort == 0:
   print("Richtiges Passwort")
else:
   print("Falsches Passwort")
   exit()
  

Alter = int(input(("Glücksspiel ist Ab 18. Bitte geben sie ihr Alter ein:  ")))
if Alter < 18:
   print("zu Jung komm wieder wenn du alt genug bist ")
   exit()
else:
   print ("Alt genug es geht weiter")

Spiel = str(input("Soll es Los gehen?: "))

print("Dealers Hand")

print(Dealer + Dealer2)

print("Deine Hand")

print(Spieler + Spieler2)
Dealer5 = Dealer2 + Dealer
Spieler4 = Spieler+ Spieler2
Dealer4 = Dealer + Dealer2

if Dealer4 > 21:
   print("Dealer hat überschritten, Du Gewinnst!" ) 
   exit()
elif Spieler4 > 21:
   print("Dealer hat überschritten Du hats Gewonnen")
   exit()
elif Dealer4 <= 16:
   print("Dealer muss eine Karte Ziehen!:" ) 
   print(Dealer3 + Dealer2 + Dealer)
else:
   print("Der Dealer muss nicht Ziehen!")

Dealer4 = Dealer + Dealer2 + Dealer
Nachfrage = str(input("Willst du noch eine Karte Ziehen?: "))
if Nachfrage == "Ja":
 print("Deine Hand")
 print(Spieler + Spieler2 + Spieler3)
 print("Dealers Hand")
 print(Dealer + Dealer2 + Dealer3)
else:
    print("Dann Mal Sehen wer gewonnen Hat")

Spieler = Spieler + Spieler2 + Spieler3
Dealer = Dealer + Dealer2 + Dealer3
input("Hmmm.... Willst du es wirklich sehen?: ")
if Dealer > 21:
   print("Dealer hat überschritten, Du hast Gewonnen!")
elif Spieler > 21:
   print("Du hast überschritten, Der  Dealer hat gewonnen!")
elif Dealer < Spieler:
   print("Du hast Gewonnen!")
elif Spieler < Dealer:
   print("Dealer Gewinnt")
else:
   print("unentschiedem")


print("Programm ende!")




