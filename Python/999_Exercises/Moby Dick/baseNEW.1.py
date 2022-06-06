x=0
with open('moby.txt') as f:
    for line in f:
        sentence = line.strip()
        for i in range(0,len(sentence)):
            if sentence[i:i+5].lower()=='whale':
                x=x+1
print("The amount of times (whales) is said is " + str(x) + " times")
f.close()
