data = open("E:\CodingStuff\AdventOfCode\Day6imput.txt")
data = data.read()
data = data.split(",")

len(data)
class fish:
    def __init__(self, countdown):   
        self.count = len(countdown)
        self.countdown = [int(x) for x in countdown]
    
    def day(self):
        for num in range(len(self.countdown)):
            if(self.countdown[num] == 0):
                self.countdown.append(8)
                self.countdown[num] = 6
            else:
                self.countdown[num]-=1

newfish = fish(data)

for c in range(256):
    newfish.day()

print(len(newfish.countdown))
