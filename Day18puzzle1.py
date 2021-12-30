data = open("E:\CodingStuff\AdventOfCode\Day18imput.txt")
data = data.readlines()
data = [x.strip("\n") for x in data]


#[[3,9],[[4,[5,5]],[9,4]]]
def createline(line):
    print(line)
    output = []
    pos=1
    while(pos<len(line)-1):
        try:
            output.append(int(line[pos]))
        except:
            if(line[pos]=="["):
                start=pos
                stack=0
                for x in range(pos+1, len(line)):
                    if(line[x]=="["):
                        stack+=1
                    elif(line[x]=="]" and stack>0):
                        stack-=1
                    elif(line[x]=="]" and stack==0):
                        iter = line[pos:x+1]
                        pos=x+1
                        output.append(createline(iter))
                        break
        pos+=1
    return(output)

print(createline(data[1]))

print("\n\n\n\n")

def addnums(num1, num2):
    return [num1, num2]

def addcode(code):
    for x in range(len(code)):
        if(code[-(x+1)]=="0"):
            code[-(x+1)]="1"
            return code
        if(code[-(x+1)]=="1"):
            code[-(x+1)]="0"
    return(False)

def subcode(code):
    for x in range(len(code)):
        if(code[-(x+1)]=="1"):
            code[-(x+1)]="0"
            return code
        if(code[-(x+1)]=="0"):
            code[-(x+1)]="1"
    return(False)

def explode(num, explcode):
    
    #pop up
    loc = explcode.copy()
    loc.append("1")
    toadd = num[int(explcode[0])][int(explcode[1])][int(explcode[2])][int(explcode[3])][1]
    loc = addcode(loc)
    if(loc):
        try:
            num[int(loc[0])][int(loc[1])][int(loc[2])][int(loc[3])][int(loc[4])] += toadd
        except:
            try:
                num[int(loc[0])][int(loc[1])][int(loc[2])][int(loc[3])] += toadd
            except:
                try:
                    num[int(loc[0])][int(loc[1])][int(loc[2])] += toadd
                except:
                    try:
                        num[int(loc[0])][int(loc[1])] += toadd
                    except:
                        try:
                            num[int(loc[0])] += toadd
                        except:
                            print("did a boo boo explode")
    
    #pop down
    loc = explcode.copy()
    loc.append("0")
    toadd = num[int(explcode[0])][int(explcode[1])][int(explcode[2])][int(explcode[3])][0]
    loc = subcode(loc)
    if(loc):
        try:
            num[int(loc[0])][int(loc[1])][int(loc[2])][int(loc[3])][int(loc[4])] += toadd
        except:
            try:
                num[int(loc[0])][int(loc[1])][int(loc[2])][int(loc[3])] += toadd
            except:
                try:
                    num[int(loc[0])][int(loc[1])][int(loc[2])] += toadd
                except:
                    try:
                        num[int(loc[0])][int(loc[1])] += toadd
                    except:
                        try:
                            num[int(loc[0])] += toadd
                        except:
                            print("did a boo boo explode")
    num[int(explcode[0])][int(explcode[1])][int(explcode[2])][int(explcode[3])] = 0
    return(num)

def split(num):
    loc=["0","0","0","0"]
    x=True
    while(x==True):
        if(loc):
            try:
                if(num[int(loc[0])][int(loc[1])][int(loc[2])][int(loc[3])]>9):
                    if(num[int(loc[0])][int(loc[1])][int(loc[2])][int(loc[3])]%2==0):
                        num[int(loc[0])][int(loc[1])][int(loc[2])][int(loc[3])] = [num[int(loc[0])][int(loc[1])][int(loc[2])][int(loc[3])]//2, num[int(loc[0])][int(loc[1])][int(loc[2])][int(loc[3])]//2]
                    else:
                        num[int(loc[0])][int(loc[1])][int(loc[2])][int(loc[3])] = [num[int(loc[0])][int(loc[1])][int(loc[2])][int(loc[3])]//2, num[int(loc[0])][int(loc[1])][int(loc[2])][int(loc[3])]//2+1]
                    return num
                
            except:
                try:
                    if(num[int(loc[0])][int(loc[1])][int(loc[2])]>9):
                        if(num[int(loc[0])][int(loc[1])][int(loc[2])]%2==0):
                           num[int(loc[0])][int(loc[1])][int(loc[2])] = [num[int(loc[0])][int(loc[1])][int(loc[2])]//2, num[int(loc[0])][int(loc[1])][int(loc[2])]//2]
                        else:
                            num[int(loc[0])][int(loc[1])][int(loc[2])] = [num[int(loc[0])][int(loc[1])][int(loc[2])]//2, num[int(loc[0])][int(loc[1])][int(loc[2])]//2+1]
                        return num
                except:
                    try:
                        if(num[int(loc[0])][int(loc[1])]>9):
                            if(num[int(loc[0])][int(loc[1])]%2==0):
                               num[int(loc[0])][int(loc[1])] = [num[int(loc[0])][int(loc[1])]//2, num[int(loc[0])][int(loc[1])]//2]
                            else:
                                num[int(loc[0])][int(loc[1])] = [num[int(loc[0])][int(loc[1])]//2, num[int(loc[0])][int(loc[1])]//2+1]
                            return num
                    except:
                        try:
                            if(num[int(loc[0])]>9):
                                if(num[int(loc[0])]%2==0):
                                    num[int(loc[0])] = [num[int(loc[0])]//2, num[int(loc[0])]//2]
                                else:
                                   num[int(loc[0])] = [num[int(loc[0])]//2, num[int(loc[0])]//2+1]
                                return num
                        except:                        
                            print("did a boo boo split")
            loc = addcode(loc)
        else:
            x=False
    return False

def findexplode(num):
    loc = ["0", "0", "0", "0"]
    x=True
    while(loc!=False):
        try:
            y=num[int(loc[0])][int(loc[1])][int(loc[2])][int(loc[3])][0]
            return loc
        except:
            loc = addcode(loc)
    return False



def reducenums(line):
    while(True):
        explodeloc = findexplode(line)
        print(explodeloc)
        if(explodeloc!=False):
            line = explode(line, explodeloc)
            continue
        splitresult = split(line)
        if(splitresult!=False):
            line = splitresult
            continue
        break
    return line

def findmagnitude(line):
    print("hi")
    try:
        print(line[0]+2)
        print(line[1]+2)
        print("passed first try")
        return 3*line[0]+2*line[1]
    except:
        try:
            print(line[0]+2)
            print("passed second try")
        except:
            line[0]=findmagnitude(line[0])
        try:
            print(line[1]+2)
            print("passed third try")
        except:
            line[1]=findmagnitude(line[1])
    return(3*line[0]+2*line[1])


numlist = []
for line in data:
    numlist.append(createline(line))
for line in numlist:
    print(line)
sum = numlist[0]
for line in range(len(numlist)-1):
    sum = addnums(sum, numlist[line+1])
    print(sum)
    sum=reducenums(sum)
    
print(sum)
    
print(findmagnitude(sum))
