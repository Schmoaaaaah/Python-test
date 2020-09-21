def main():
  print("Hello World")
  Name = input("Wie heißt du? \n")
  print("Hallo " + Name + ".")
  if(Name == "Max"):
    i=0
    for i in range(1,30):
      print(Name + " ist blöd")
  elif(Name == "Noah"):
    print(Name + " ist voll nett")

def Variablen():
  hallo = "Hallo"
  Name = "Noah"
  print(2*(hallo+Name))
  foo ="foo"
  print(foo)
  print(type(foo))
  foo = 1
  print(foo)
  print(type(foo))

def Listen():
  import random
  lul = ["Hallo","Hi","Guten Tag"]
  print(random.uniform(0,len(lul)))
  print("begruesung " + lul[0])

def Schmeicheln():
  import random
  import os
  adjektiv = ["beste","schönste","schlauste","schnellste"]
  nomen = ["Mensch","Freund","Lehrer"]

  def menue():
    os.system('clear') ##😔
    auswahl = int(input("1 = adjektiv hinzufügen; 2 = nomen hinzufügen; 3 = random ausgabe"))
    if auswahl == 1:
      addadj()
    elif auswahl == 2:
      addnom()
    elif auswahl == 3:
      ausgabe()
    else:
      print("fehlerhafte eingabe! Tschüsss")


  def ausgabe():
    print("Du bist der " + random.choice(adjektiv) + " " + random.choice(nomen) + "!")
    menue()

  def addadj():
    adjektiv.append(input("Welches Adjektiv soll hinzugefügt werden?"))
    menue()
  
  def addnom():
    nomen.append(input("Welches Nomen soll hinzugefügt werden?"))
    menue()
  
  menue()

def RGBtoCMYK():
  def rgbinput():
  farbe = input("Welche Farbe(C,M,Y,K).")
  rgbcode = input("Geben sie die RGB Farbcodes ein(Komma getrennt(R,G,B)).")
  farbcodes = []
  farbcodes.extend(rgbcode.split(","))
  cmyk = rgbtocmyk(rgbcode,farbe)
  print("Der CMYK Code ist: "+str(cmyk))
  
  def rgbtocmyk(rgb,farbe):
    if(farbe == "K"):
      
    else:
      cmyk=0
    return cmyk
  
  rgbinput()

RGBtoCMYK()