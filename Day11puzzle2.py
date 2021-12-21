data = open("E:\CodingStuff\AdventOfCode\Day11imput.txt")
data = data.readlines()
for row in range(len(data)):
    data[row] = data[row].strip("\n")
data = [list(x) for x in data]
data = [[int(c) for c in x] for x in data]
print(len(data))
print(len(data[0]))

class octgrid:
    def __init__(self, data):
        self.data=data
        self.count=0

    def day(self):
        self.flashlist = []
        for row in range(len(self.data)):
            for col in range(len(self.data[0])):
                self.data[row][col]+=1
        
        for row in range(len(self.data)):
            for col in range(len(self.data[0])):
                if(self.data[row][col]>9 and (not ([row,col] in self.flashlist))):
                    self.flash(row, col)
        for row in range(len(self.data)):
            for col in range(len(self.data[0])):
                if([row,col] in self.flashlist):
                    self.data[row][col] = 0
        return(len(self.flashlist))
                    
                    

                

    def flash(self, row, col):
        self.count+=1
        self.flashlist.append([row,col])
        for x in range(-1,2):
            for y in range(-1,2):
                file = row+x
                colunm = col+y
                if((file<len(self.data) and file>-1)):
                    if((colunm<len(self.data[0]) and (colunm)>-1)):
                        self.data[file][colunm]+=1 
                        if((not ([file,colunm] in self.flashlist)) and self.data[file][colunm]>9):
                            self.flash(file, colunm)

grid = octgrid(data)
b=0
cheese=True
while cheese:
    b+=1
    if(grid.day()==100):
        cheese=False
        print(b)



