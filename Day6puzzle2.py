data = open("E:\CodingStuff\AdventOfCode\Day6imput.txt")
data = data.read()
data = data.split(",")

len(data)
class fish:
    def __init__(self, countdown):   
        self.count = len(countdown)
        self.countdown = [int(x) for x in countdown]
        self.eight = 0
        self.seven = 0
        self.six = 0
        self.five = 0
        self.four = 0
        self.three = 0
        self.two = 0
        self.one = 0
        self.zero = 0
        for num in self.countdown:
            if num==8:
                self.eight+=1
            if num==7:
                self.seven+=1
            if num==6:
                self.six+=1
            if num==5:
                self.five+=1
            if num==4:
                self.four+=1
            if num==3:
                self.three+=1
            if num==2:
                self.t+=1
            if num==1:
                self.one+=1
            if num==0:
                self.zero+=1
    
    def day(self):
        temp = self.zero
        self.zero = self.one
        self.one = self.two
        self.two = self.three
        self.three = self.four
        self.four = self.five
        self.five = self.six
        self.six = self.seven+temp
        self.seven = self.eight
        self.eight = temp

newfish = fish(data)

for c in range(256):
    newfish.day()

print(newfish.eight+newfish.seven+newfish.six+newfish.five+newfish.four+newfish.three+newfish.two+newfish.one+newfish.zero)
