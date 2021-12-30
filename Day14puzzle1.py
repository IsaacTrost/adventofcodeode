data = open("E:\CodingStuff\AdventOfCode\Day14imput.txt")
data = data.readlines()

imput=data[0].strip("\n")
rules = data[2:]

rules = [x.strip("\n").split(" -> ") for x in rules]

def step(imput, rules, pie):
    output = ""
    print(pie)
    for num in range(len(imput)-1):
        pair = imput[num:num+2]
        output+=pair[0]
        for x in rules:
            if x[0]==pair:
                if(pie==0):
                    print(str(num) + x[1])
                output+=x[1]
    output+=imput[-1]
    return output
for rule in range(len(rules)):
    final = rules[rule][0]
    for cheese in range(40):
        final=step(final, rules, cheese)
    rules[rule].append
print(rules)
charlist = []

for char in imput:
    c=True
    for cheese in range(len(charlist)):
        if char==charlist[cheese][0]:
            charlist[cheese][1]+=1
            c=False
    if c:
        charlist.append([char, 1])

print(charlist)
min = 1000000
max=0
for char in charlist:
    if(char[1]>max):
        max=char[1]
    elif(char[1]<min):
        min=char[1]
print(max-min)
