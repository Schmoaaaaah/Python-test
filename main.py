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
  def inputrgb():
    farbe = input("Welche Farbe(C,M,Y,K).")
    rgbcode = input("Geben sie die RGB Farbcodes ein(Komma getrennt(R,G,B)).")
    farbcodes = []
    farbcodes.extend(rgbcode.split(","))
    cmyk = rgbtocmyk(farbcodes,farbe)
    print("Der CMYK Code für "+farbe+" ist: "+str(cmyk))
  
  def rgbtocmyk(rgb,farbe):
    r = int(rgb[0])
    g = int(rgb[1])
    b = int(rgb[2])
    w = max(r/255, g/255, b/255)
    if(farbe == "K"):
      cmyk=1-w
    elif(farbe == "C"):
      cmyk=(w-(r/255))/w
    elif(farbe == "M"):
      cmyk=(w-(g/255))/w
    elif(farbe== "Y"):
      cmyk=(w-(b/255))/w
    else:
      print("Fehler in Rechnung.")
    return cmyk
  
  inputrgb()

def zahleninput():
  zahlen = []
  zahl = input("Geben Sie drei Zahlen durch Komma getrent ein(1,2,3).")
  zahlen.extend(zahl.split(","))
  ergebnis = zahlensortieren(zahlen)
  print("Die größte Zahl ist: "+str(ergebnis)+".")
  
def zahlensortieren(zahl):
  zahlen = [int(i) for i in zahl]
  if(zahlen[0]>zahlen[1] and zahlen[0]>zahlen[2]):
    return zahlen[0]
  elif(zahlen[1]>zahlen[0] and zahlen[1]>zahlen[2]):
    return zahlen[1]
  elif(zahlen[2]>zahlen[0] and zahlen[2]>zahlen[1]):
    return zahlen[2]
  else:
    print("Einige Zahlen waren gleich und konnten somit nicht bestimmt werden")

def summeberechnen():
  def eingabe():
    first = input("Geben sie die Anfangszahl ein")
    end = input("Geben sie die letze Zahl ein")
    print("Sie beginnen mit "+first+" und enden mit "+end+".")
    summe = rechnung(int(first),int(end)+1)
    print("Die Summe ist: "+str(summe))


  def rechnung(first,end):
    summe = first
    for i in range(first,end):
      summe = summe + i
    print("count: "+str(i))
    return summe;
  eingabe()

def domino():
  def dynamic():
    last = input("Bis wo sollen die Zahlen gehen? :")
    seperator = input("Wo durch sollen die Zahlen getrennt werden? :")
    dominosteine(last,seperator)

  def dominosteine(last,seperator):
    start = 0
    space = (len(last)+len(seperator)+4)*" "
    if(int(last)>=1):
      for i in range(start,int(last)+1):
        print(i*space,end = "")
        for y in range(i,int(last)+1):
          print("("+str(i)+"|"+str(y)+")",end = seperator)
        print("")
    else:
      print("Die Zahl ist zu klein!")
      dynamic()

  dynamic()
  
def test():
  import random
  lul = ["Hallo","Test"]
  lul = lul.add("bro")
  print(random.uniform(0,10))

test()