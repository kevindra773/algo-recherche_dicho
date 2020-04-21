from random import *
x =randint(0,100)
y=int(input("Trouve le nombre entre 0 et 100"))
z=0
while y!=x and z<7:
  z=z+1
  if y<=x:
    y=int(input("Le nombre recherché est plus grand"))
  else:
    y=int(input("Le nombre recherché est plus petit"))
if x==y:
  print ("bravo c'est bien "+str(x))
else:
  print("Tu est vraiment nul , la bon chiffre est  "+str(x))