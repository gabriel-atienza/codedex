#variables
gryffindor = 0
ravenclaw = 0
hufflepuff = 0
slytherin = 0

q1 = int(input("Q1) Do you like Dawn or Dusk?\n1) Dawn\n2) Dusk\n"))
if q1 == 1:
  gryffindor = gryffindor + 1 
  ravenclaw = ravenclaw + 1
elif q1 == 2:
  hufflepuff = hufflepuff + 1
  slytherin = slytherin + 1
else:
  print("Wrong input. ")

q2 = int(input("Q2) When I'm dead, I want people to remember me as:\n1) The Good\n2) The Great\n3) The Wise\n4) The Bold\n"))
if q2 == 1:
  hufflepuff = hufflepuff + 2
elif q2 == 2:
  slytherin = slytherin + 2
elif q2 == 3:
  ravenclaw = ravenclaw + 2
elif q2 == 4:
  gryffindor = gryffindor + 2
else:
  print("Wrong input. ")

q3 = int(input("Q3) Which kind of instrument most pleases your ear?\n1) The violin\n2) The trumpet\n3) The piano\n4) The drum\n"))
if q3 == 1:
  slytherin = slytherin + 4
elif q3 == 2:
  hufflepuff = hufflepuff + 4
elif q3 == 3:
  ravenclaw = ravenclaw + 4
elif q3 == 4:
  gryffindor = gryffindor + 4
else:
  print("Wrong input. ")

print("you scored " + str(gryffindor) + " gryffindor points.") 
print("you scored " + str(ravenclaw) + " ravenclaw points.")
print("you scored " + str(hufflepuff) + " hufflepuff points.")
print("you scoreed " + str(slytherin) + " slytherin points.")