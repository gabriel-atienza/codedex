#while loop that continues until the system rolls a 1 and a 1
import random

die1 = random.randint(1, 6)
die2 = random.randint(1, 6)
total = die1 + die2

while total != 2:
  print("Nope")
  die1 = random.randint(1, 6)
  die2 = random.randint(1, 6)
  total = die1 + die2

print("Snake eyes!")