x = int(input("Please enter the first number: "))
o = str(input("Please enter an operation: "))
y = int(input("Please enter the second number: "))
if(o=='+'):
    print(str(x)+"+"+str(y)+"="+str(x+y))
elif(o=='-'):
    print(str(x)+"-"+str(y)+"="+str(x-y))
elif(o=='*'):
    print(str(x)+"*"+str(y)+"="+str(x*y))
else:
    print(str(x)+"/"+str(y)+"="+str(x/y))
    