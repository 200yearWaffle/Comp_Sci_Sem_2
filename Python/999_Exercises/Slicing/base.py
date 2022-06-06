x = input("Please input your first and last name: ")
j=1
for s in range(0, 1):
    for i in range(0,len(x)):
        y=x[i:j]
        j=j+1
        print(y)
    print("")
if (i!=" "):
    fs=1
    for t in range(0,len(x)):
        k=x[t:fs]
        fs=fs+1
        if (k==" "):
            print("The space's index was " + str(t))
            break
for b in range(t, len(x)):
    print(x[b:b+1])
print(" ")
for m in range(0, t):
    print(x[m:m+1])