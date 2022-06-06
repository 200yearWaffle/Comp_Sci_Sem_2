import random
list_r=["CPK","KCC","PYT"]
list_c=["pasta","chicken","salad"]
list_k=["beef","fruit salad","soup"]
list_p=["steak","pork","baguette"]
z = int(random.randrange(3))
x = input("pick a restaurant(CPK,KCC,PYT): ")
if x == 'CPK':
    print("Thanks for chosing CPK, here is the menu: " + str(list_c))
    if z == 0:
        print("We suggest the " + list_c[0])
    elif z == 1:
        print("We suggest the " + list_c[1])
    else: 
        print("We suggest the " + list_c[2])
elif x == 'KCC':
    print("Thanks for chosing KCC, here is the menu: " + str(list_k))
    if z == 0:
        print("We suggest the " + list_k[0])
    elif z == 1:
        print("We suggest the " + list_k[1])
    else: 
        print("We suggest the " + list_k[2])
elif x == 'PYT':
    print("Thanks for chosing PYT, here is the menu: " + str(list_p))
    if z == 0:
        print("We suggest the " + list_p[0])
    elif z == 1:
        print("We suggest the " + list_p[1])
    else: 
        print("We suggest the " + list_p[2])
else:
    print("That is not an option, run again")