data = open("E:\CodingStuff\AdventOfCode\Day7imput.txt")
data = data.read()
data = data.split(",")
data = [int(x) for x in data]

class sub:
    def __init__(self, data):
        self.data=data
    def findmean(self):
         mean = sum(self.data)/len(self.data)
         self.mean = round(mean)
         return(self.mean)
    def calcfuel(self, value):
        indcosts = [sub.calc1fuel(x, value) for x in self.data]
        fuelcost = sum(indcosts)
        return fuelcost
    def calc1fuel(position, target):
        diff = abs(position-target)
        c=0
        for x in range(diff):
            c+=(x+1)
        return c
    def findlowest(self):
        x=self.mean
        while True:
            if(self.calcfuel(x)>self.calcfuel(x-1)):
                x-=1
            elif((self.calcfuel(x)>self.calcfuel(x+1))):
                x+=1
            else:
                return self.calcfuel(x)




subs = sub(data)
subs.findmean()
print(subs.findlowest())