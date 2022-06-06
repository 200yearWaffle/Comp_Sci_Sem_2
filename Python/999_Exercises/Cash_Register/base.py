x = int(input("How many items are you purchasing(1-5)?: "))
sum = 0
for a in range(0,x):
    ilist = str(input("What item are you purchasing?: "))
    m = float(input("How much is this item?: "))
    print("Thanks for purchasing " + ilist+ "!")
    print("_______________________________________")
    sum = sum + m
if x>1:
    print("For " + str(x) + " items, your total is: $" + str(sum))
    print("Have a nice day! Please come again!")
elif x<2:
    print("For " + str(x) + " item, your total is: $" + str(sum))
    print("Have a nice day! Please come again!")
print("You purchased: ")