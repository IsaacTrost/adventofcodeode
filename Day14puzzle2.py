data = open("E:\CodingStuff\AdventOfCode\Day14imput.txt")
data = data.readlines()

imput=data[0].strip("\n")
rules = data[2:]

rules = [x.strip("\n").split(" -> ") for x in rules]

def step(imput, rules, pie, iter):
    output = ""
    print(pie)
    for num in range(len(imput)-1):
        pair = imput[num:num+2]
        output+=pair[0]
        for x in rules:
            if x[0]==pair:
                output+=x[iter]
    output+=imput[-1]
    return output

iter=1
while(iter<6):
    for rule in range(len(rules)):
        if iter==1:
            cake=0
        else:
            cake=iter
        final = rules[rule][cake]
        for cheese in range(10):
           final=step(final, rules, cheese, iter)

        rules[rule].append(final[1:-1])
        print(iter)
    iter+=1



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
min = 10000000000
max=0
for char in charlist:
    if(char[1]>max):
        max=char[1]
    elif(char[1]<min):
        min=char[1]
print(max-min)
