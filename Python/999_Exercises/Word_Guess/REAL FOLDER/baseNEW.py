import random
list_a=[]
with open('allow_words.txt') as f:
    for line in f:
        l = line.strip()
        list_a.append(1)
n=int(random.randomnumber(12972))
k=list_a[n]
print(k)
for i in range(0,6):
    x = input("Please guess a random (5 letter)word: ")
    if x==k:
        print("You got the correct answer!")
        break
    else:
         for word in list_a:
            if x == a:
                t = 1
            if t==1:
                print("wrong word")
        else:
            print("You gussed wrong, try again!")
print("You have ran out of tries, the word was " + k)
f.close()
