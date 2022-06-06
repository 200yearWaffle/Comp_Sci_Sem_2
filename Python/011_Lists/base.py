import random
list=["THIS IS THE GREATEST PLAANNN!", "WHAT 9+10? 21!", "MY NAME IS JEFF!", "YOU ACTIVATED MY TRAP CARD! UNO REVERSE CARD!", "NO YOU!"]
x = int(random.randrange(5))
if x==0:
    print(list[0])
elif x==1:
    print(list[1])
elif x==2:
    print(list[2])
elif x==3:
    print(list[3])
else:
    print(list[4])