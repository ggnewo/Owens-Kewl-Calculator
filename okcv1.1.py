import math
import time

print("Welcome to Owen's Kewl Calculator.")
m1 = ""
m2 = ""
n1 = ""
n2 = ""
n1p1 = ""
n1p2 = ""
n2p1 = ""
n2p2 = ""
cm = ""
rpsolve = ""

def ss():
  global m1
  global m2
  global n1
  global n2
  print("If you haven't used this   before, I would suggest typing ? in \n the first box to learn the UI.")
  num1 = 0
  num2 = 0
  explain1 = "First, decide if you want area or parimater by typing a or p. If you're doing midpoints, leave this blank. Type ? in \nthe next box \nfor more info.  "
  explain2 = "For different shapes, just type the first letter of the \nshape in lowercase. For example, t would be  triangle. Currently, I have \nrectangle ,triangles, and midpoints, but I'll be adding more :). If you do midpoints leave the other numbers blank after you put \nyour order pair in."
  m1 = input("Area or Perimiter? ")
  m2 = "0"
  if m1 == "?":
    print(explain1)
    print(" ")
    print(explain2)
    print("0")
    print("Please restart now.")
  else:
    m2 = input("What shape? ")
  if m2 == "0":
    print("You discovered a secret. Good for you")
  else:
    n1 = input("What's your first number? ")
    n2 = input("What's your second number? ")
def ms():
    global n1p1
    global n1p2
    global n2p1
    global n2p2
    n1p1 = input("What's your first x value? ")
    n1p2 = input("What's your first y value? ")
    n2p1 = input("What's your second x value? ")
    n2p2 = input("What's your second y value? ")
    m1 = "nothing kekw"
    m2 = "same"
def dfss():
  global num1
  global num2
  global num3
  global num4
  num1 = input("What's the first x value? ")
  num2 = input("What's the second x value? ") 
  num3 = input("What's the first y value? ")
  num4 = input("What's the second y value? ")
def mm():
  global cm
  print(" ")
  print("Please select your mode")
  print("sf = Shape Formulas")
  print("m = Midpoints")
  print("df = Distance Formula")
  print(" ")
  cm = input("")
  if cm == "sf":
    ss()
  elif cm == "m":
    ms()
  elif cm == "df":
    dfss()
def dia():
  print("nothing, for now.")
#----------------
mm()
#----------------
def recper():
  rpsolve1 = int(n1) + int(n2)
  rpsolve2 = rpsolve * 2
  print(" ")
  print(" ")
  print(" ")
  print("Your answer is:")
  print(rpsolve2)
def recare():
  rasolve = int(n1) * int(n2)
  print(" ")
  print(" ")
  print(" ")
  print("Your answer is:")
  print(rasolve)
def triper():
  tpsolve = int(n1) + int(n2)
  print(" ")
  print(" ")
  print(" ")
  print("Your answer is:")
  print(tpsolve)
def triare():
  tasolve1 = int(n1) * int(n2)
  tasolve2 = tasolve1 / 2
  print(" ")
  print(" ")
  print(" ")
  print("Your answer is:")
  print(tasolve2)
def mps():
    msp1 = int(n1p1) + int(n2p1)
    msp2 = msp1 / 2
    msp3 = int(n1p2) + int(n2p2)
    msp4 = msp3 / 2
    print("The answer is")
    print("(" + str(msp2) + "," + str(msp4) + ")")
def dfs():
  print(" ")
  print("(" + str(num1) + "," + str(num2) + ") (" + str(num3) + "," + str(num4) + ")")

  uno = int(num1) - int(num2)
  dos = int(num3) - int(num4)

  print("(" + str(uno) + ") (" + str(dos) + ")") 

  tres = uno * uno
  quatro = dos * dos

  print("(" + str(tres) + "+" + str(quatro) + ")")

  cinco = tres + quatro

  print("(" + str(cinco) + ")")

  fin = math.sqrt(cinco)
  print("The asnwer is:")
  print(fin)
  dia()
#-----------------
def shapesolve():
  if m1 == "p" and m2 == "r":
    recper()
  elif m1 == "a" and m2 == "r":
    recare()
  elif m1 == "p" and m2 == "t":
    triper()
  elif m1 == "a" and m2 == "t":
    triare()
  elif cm == "m":
    mps()
  elif cm == "df":
    dfs()
  else:
    print("There was an error. Please type y to try again")
    dummy = input(" ")
    if dummy == "y" or "Y":
      print(" ")
      print(" ")
      print(" ")
      mm()
    else:
      print("Bro you're so dumb :skull:")
#-----------------
shapesolve()
