x = int(input("How long do you want the line to be(1-10)? "))
y = input("vertical or horizontal(v or h)? ")
if y=="v":
    for l in range(0,x):
        print("_")
if y=="h":
    for lh in range(0,x):
        print("_" ,end="")