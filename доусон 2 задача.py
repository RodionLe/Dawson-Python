import random
eagle = 0
tails = 0
tries = 0
while tries != 100:
   x = random.randint(1,2)
   tries += 1
   if x == 1:
       eagle += 1
   elif x == 2:
       tails += 1
print("Орел выпал:", eagle, "а решка выпала:", tails)        

