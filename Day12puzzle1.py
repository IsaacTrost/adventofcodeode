data = open("E:\CodingStuff\AdventOfCode\Day12imput.txt")
data = data.readlines()
data = [x.strip("\n").split("-") for x in data]

class cave:
    def __init__(self, letter, data):
        self.id = letter
        self.connections = []
        for row in data:
            
            if(row[0]==self.id):
                self.connections.append(row[1])
            if(row[1]==self.id):
                self.connections.append(row[0])
        self.big=False
        if (self.id==self.id.upper()):
            self.big=True

cavedict = {}

caveidlist = []
for row in data:
    for col in row:
        if col not in caveidlist:
            caveidlist.append(col)
            cavedict[col] = cave(col, data)


class paths:
    def __init__(self, cavedict):
        self.cavelist = cavedict
        self.optionslist = [[len(cavedict["start"].connections)-1, "start"]]
        self.path = [cavedict["start"]]
        self.count=0
    
    def genpath(self):
        self.restricted = [cavedict["start"]]
        self.path = [cavedict["start"]]
        if(self.optionslist[0][0]>-1):
            while(self.poplast()):
                x=1
            x=0
            while(self.addcave(x)):
                print(len(self.optionslist))
                print(x)
                print(self.path[-1].id)
                x+=1
                if(self.path[-1].id=="end"):
                    self.count+=1
                    break
           
            return True
        return False
            


        

    def addcave(self, x):
        if(cavedict[self.path[-1].connections[self.optionslist[x][0]]] not in (self.restricted)):
            self.path.append(cavedict[self.path[-1].connections[self.optionslist[x][0]]])
            if not self.path[-1].big:
                    self.restricted.append(self.path[-1])
            if(self.path[-1].id!="end" and len(self.optionslist)<len(self.path)):
                self.optionslist.append([len(self.path[-1].connections)-1, self.path[-1].id])
            else:
                self.optionslist[-1][0]-=1
            return True
        self.optionslist[-1][0]-=1
        return False
    
    def poplast(self):
        if(self.optionslist[-1][0]<0):
            self.optionslist.pop()
            self.optionslist[-1][0]-=1
        if(self.optionslist[-1][0]<0):
            return True
        return False

pathgen = paths(cavedict)
while(pathgen.genpath()):
    x=1
print(pathgen.count)

        


