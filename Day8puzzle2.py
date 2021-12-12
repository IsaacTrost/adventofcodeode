data = open("E:\CodingStuff\AdventOfCode\Day8imput.txt")
data = data.readlines()

class display:
    def __init__(self, line):
        line = line.split(" ")
        
        self.output = line[11:15]
        self.numbers = line[0:10]
        self.output[3]=self.output[3].strip("\n")
    def finddigits(self):
        for row in range(len(self.numbers)):
            self.numbers[row] = sorted(self.numbers[row])
        for digit in self.numbers:
            if(len(digit)==2):
                self.one = digit
            if(len(digit)==4):
                self.four = digit
            if(len(digit)==7):
                self.eight = digit
            if(len(digit)==3):
                self.seven = digit
        self.numbers.remove(self.one)
        self.numbers.remove(self.four)
        self.numbers.remove(self.eight)
        self.numbers.remove(self.seven)
        self.top = self.finddiffchars(self.seven, self.one)[0]
        for digit in self.numbers:
            if(len(digit)==6):
                if(len(self.findsamechars(digit, self.one))==1):
                    self.six=digit
        self.numbers.remove(self.six)
        self.bottemright = self.findsamechars(self.six, self.one)[0]
        self.topright = self.finddiffchars(self.one, self.six)[0]
        for digit in self.numbers:
            if(len(digit)==5):
                if(len(self.findsamechars([self.topright],digit))==0):
                    self.five = digit
        self.numbers.remove(self.five)
        self.bottemleft = self.finddiffchars(self.six, self.five)[0]
        for digit in self.numbers:
            if(len(digit)==6):
                if(len(self.finddiffchars([self.bottemleft],digit))==1):
                    self.nine = digit 
        self.numbers.remove(self.nine)
        for digit in self.numbers:
            if(len(digit)==6):
                self.zero= digit
        self.numbers.remove(self.zero)
        for digit in self.numbers:
            if(len(self.findsamechars([self.bottemleft],digit))==1):
                self.two = digit 
        self.numbers.remove(self.two)
        self.three = self.numbers[0]
    def finddiffchars(self, longer, shorter):
        out = []
        for char in longer:
            counter=0
            for ch in shorter:
                if char!=ch:
                    counter+=1
            if counter==len(shorter):
                out.append(char)
        return out
    def findsamechars(self, longer, shorter):
        out = []
        for char in longer:
            counter=0
            for ch in shorter:
                if char!=ch:
                    counter+=1
            if counter<len(shorter):
                out.append(char)
        return out
    def findoutput(self):
        out = ""
        self.finddigits()
        for row in range(len(self.output)):
            self.output[row] = sorted(self.output[row])
            
        for row in self.output:
            if(row==self.one):
                print("hi")
                out+="1"
            if(row==self.two):
                out+="2"
            if(row==self.three):
                out+="3"
            if(row==self.four):
                out+="4"
            if(row==self.five):
                out+="5"
            if(row==self.six):
                out+="6"
            if(row==self.seven):
                out+="7"
            if(row==self.eight):
                out+="8"
            if(row==self.nine):
                out+="9"
            if(row==self.zero):
                out+="0"
            print(out)
        return int(out)

class displayset:
    def __init__(self, data):
        self.displaylist = []
        for row in data:
            self.displaylist.append(display(row))
    def findsum(self):
        count = 0
        for display in self.displaylist:
            count += display.findoutput()
        return count

displaylist = displayset(data)
print(displaylist.findsum())