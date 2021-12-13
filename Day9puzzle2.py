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

class basin:
    map = data
    def __init__(self, lowpoint):
        self.lowpoint = lowpoint
        self.pointlist = [lowpoint]
    
    def findsize(self):
        self.size=1
        iter = [self.lowpoint]
        while(len(iter)>0):
            temp=[]
            for point in iter:
                for point in self.fourwayextend(point):
                    temp.append(point)
            iter = temp
        return self.size
        
    def fourwayextend(self, point):
        returny = []
        if (point[0]<len(data)-1 and data[point[0]+1][point[1]]!=9 and not ([point[0]+1,point[1]] in self.pointlist)):
            self.pointlist.append([point[0]+1,point[1]])
            self.size+=1
            returny.append([point[0]+1,point[1]])
        if (point[0]!=0 and data[point[0]-1][point[1]]!=9 and not ([point[0]-1,point[1]] in self.pointlist)):
            self.pointlist.append([point[0]-1,point[1]])
            self.size+=1
            returny.append([point[0]-1,point[1]])
        if (point[1]<len(data[0])-1 and data[point[0]][point[1]+1]!=9 and not ([point[0],point[1]+1] in self.pointlist)):
            self.pointlist.append([point[0],point[1]+1])
            self.size+=1
            returny.append([point[0],point[1]+1])
        if (point[1]!=0 and data[point[0]][point[1]-1]!=9 and not ([point[0],point[1]-1] in self.pointlist)):
            self.pointlist.append([point[0],point[1]-1])
            self.size+=1
            returny.append([point[0],point[1]-1])
        return returny
        
basinlist = []
x=0
sizelist = []
for point in potentialvalues:
    basinlist.append(basin(point))
    sizelist.append(basinlist[x].findsize())
    x+=1

sizelist.sort(reverse = True)
print(sizelist)
print(sizelist[0]*sizelist[1]*sizelist[2])

            
