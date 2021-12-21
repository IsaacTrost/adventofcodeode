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
smallcavelist = []
for row in caveidlist:
    if not cavedict[row].big:
        smallcavelist[row] = row



class paths:
    def __init__(self, cavedict):
        self.cavelist = cavedict
        self.optionslist = []
        self.path = [cavedict["start"]]
    
    def genpath(self):
        self.optionslist.append(len(cavedict["start"].connections)-1)
        restricted = []
        while True:
            if(cavedict[self.path[-1].connections[self.optionslist[-1]]] not in (restricted)):
                self.path.append(cavedict[self.path[-1].connections[self.optionslist[-1]]])
                if not self.path[-1].big:
                    restricted.append(self.path[-1])
                if(self.path[-1].id == "end"):
                    return self.path
                self.optionslist.append
    
                


        


