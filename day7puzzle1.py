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
        indcosts = [x-value for x in self.data]
        indcosts = [x if x>0 else x*-1 for x in indcosts]
        fuelcost = sum(indcosts)
        return fuelcost
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