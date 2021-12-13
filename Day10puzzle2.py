data = open("E:\CodingStuff\AdventOfCode\Day10imput.txt")
data = data.readlines()
for row in range(len(data)):
    data[row] = data[row].strip("\n")

openchars = ["<","{","[","("]
closechars = [">","}","]",")"]
scoredict = {">": 4, "}":3, "]": 2, ")":1}

class line:
    def __init__(self, line):
        self.line = line
    
    def findissue(self):
        stack = []
        for char in self.line:
            if char in openchars:
                stack.append(char)
            elif(openchars[closechars.index(char)]==stack[-1]):
                del stack[-1]
            else:
                return True
        return False
    
    def findcompletionstring(self):
        self.completionstring=""
        stack = []
        for char in self.line:
            if char in openchars:
                stack.append(char)
            elif(openchars[closechars.index(char)]==stack[-1]):
                del stack[-1]
        for char in stack:
            self.completionstring+=closechars[openchars.index(char)]
        return self.completionstring



linelist = []
x=0
for ln in data:
    linelist.append(line(ln))
    if(linelist[x].findissue()):
        del linelist[-1]
        x-=1
    x+=1

scorelist = []
i=0
print(len(linelist))
for ln in linelist:
    scorelist.append(0)
    for char in reversed(ln.findcompletionstring()):
        scorelist[i]*=5
        scorelist[i]+=scoredict[char]
    i+=1
scorelist.sort()
print(len(scorelist)//2)
print(scorelist)
print(scorelist[len(scorelist)//2])
