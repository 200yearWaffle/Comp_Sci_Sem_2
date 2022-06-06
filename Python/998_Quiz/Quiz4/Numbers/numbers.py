listmn = [6,9,32,28,15,22,3,18]
max = 0
for i in range(0,len(listmn)):
    if(max < listmn[i]):
        max = listmn[i]
print(max)
min = max
for a in range(0,len(listmn)):
    if(min > listmn[a]):
        min = listmn[a]
print(min)
sum = 0
for b in range(0,len(listmn)):
    sum=sum+listmn[b]
avg = sum/len(listmn)
print(avg)