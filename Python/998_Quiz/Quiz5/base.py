f = input("What is your favorite number?(ex: My favorite number is 42)(from 00-99) ")
a = input("What is your age? ")
for l in range(0,len(f)):
    j=f[0:1+1]
    if j==f[len(f)-len(j):len(f)]:
        print("The length of your favorite number is " + str(len(j)))
for i in range(0,len(f)-1):
    y=f[i:i+len(j)]
    if y==f[len(f)-len(y):len(f)]:
        print("Your favorite number is " + str(y))
m=int(y)*int(a)
print("When multiplied, your age and favorite number equal " + str(m) + "!")