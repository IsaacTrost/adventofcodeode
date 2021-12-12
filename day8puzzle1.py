data = open("E:\CodingStuff\AdventOfCode\Day8imput.txt")
data = data.readlines()

class display:
    def __init__(self, line):
        line = line.split(" ")
        
        self.output = line[11:15]
        self.numbers = line[0:10]
        self.output[3]=self.output[3].strip("\n")
    def finduniquenums(self):
        count = 0
        for num in self.output:
            print(len(num))
            if (len(num) == 2 or len(num) == 4 or len(num) == 7 or len(num) == 3):
                count+=1
        return count

class displayset:
    def __init__(self, data):
        self.displaylist = []
        for row in data:
            self.displaylist.append(display(row))
    def findalluniques(self):
        count = 0
        for display in self.displaylist:
            count += display.finduniquenums()
        return count

displaylist = displayset(data)
print(displaylist.findalluniques())