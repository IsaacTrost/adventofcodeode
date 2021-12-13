data = open("E:\CodingStuff\AdventOfCode\Day10imput.txt")
data = data.readlines()
for row in range(len(data)):
    data[row] = data[row].strip("\n")

openchars = ["<","{","[","("]
closechars = [">","}","]",")"]
scoredict = {">": 25137, "}":1197, "]": 57, ")":3, "0":0}

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
                return char
        return "0"

linelist = []
issuelist = []
x=0
for ln in data:
    print(ln)
    linelist.append(line(ln))
    issuelist.append(scoredict[linelist[x].findissue()])
    print("\n\n")
    x+=1

print(sum(issuelist))

    