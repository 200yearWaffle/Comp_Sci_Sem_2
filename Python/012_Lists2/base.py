import random
i = int(input("How many numbers do you want to create?"))
list = []
for l in range(0,i):
    x = int(random.randrange(10))
    list.append(x)
print("You're numbers are: " + str(list))