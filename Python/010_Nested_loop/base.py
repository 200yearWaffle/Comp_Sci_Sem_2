s = input("What symbol would you like? ")
w = int(input("What is the width? "))
l = int(input("What is the length? "))
for x in range(0,w):
    for y in range(0,l):
        print(s, end="")
    print("")