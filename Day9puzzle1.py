data = open("E:\CodingStuff\AdventOfCode\Day9imput.txt")
data = data.readlines()
for row in range(len(data)):
    data[row] = data[row].strip("\n")
data = [list(x) for x in data]
data = [[int(c) for c in x] for x in data]
potentialvalues = []
#finding points smaller than those above them
for col in range(len(data)):
    for row in range(len(data[0])):
        if (col!=0):
            if(data[col][row]<data[col-1][row]):
                potentialvalues.append([col,row])
        else:
            potentialvalues.append([col,row])
print(potentialvalues)

cheese = []
#finding points smaller than those below them
for point in potentialvalues:
    if(point[0]<len(data)-1):
        if(data[point[0]][point[1]]>=data[point[0]+1][point[1]]):
            cheese.append(point)
for point in cheese:
    potentialvalues.remove(point)
cheese = []
for point in potentialvalues:
    if(point[1]!=0):
        if(data[point[0]][point[1]]>=data[point[0]][point[1]-1]):
            cheese.append(point)
for point in cheese:
    potentialvalues.remove(point)
cheese = []

for point in potentialvalues:
    if(point[1]<len(data[0])-1):
        if(data[point[0]][point[1]]>=data[point[0]][point[1]+1]):
            cheese.append(point)
for point in cheese:
    potentialvalues.remove(point)


#finding the danger
sum=0
for point in potentialvalues:
    sum+=data[point[0]][point[1]]+1

print(sum)



