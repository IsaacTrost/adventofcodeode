data = open("E:\CodingStuff\AdventOfCode\Day13imput.txt")
data = data.readlines()
x=0
for line in data:
    if line == "\n":
        break
    x+=1
points = data[0:x]
folds = data[x+1:]
points = [x.strip("\n").split(",") for x in points]
points = [[int(x) for x in y] for y in points]
folds = [x.strip("fold along \n").split("=") for x in folds]
folds = [[y[0], int(y[1])] for y in folds]
print(len(points))
def fold(points, fold):
    print(fold[1])
    xory=0
    if (fold[0]=="y"):
        xory=1
    listo = []
    for point in range(len(points)):
        if(points[point][xory]==fold[1]):
            listo.append(point)
        if(points[point][xory]>fold[1]):
            x = 2*fold[1]-points[point][xory]
            print([points[point][0], 2*fold[1]-points[point][xory]])
            if([points[point][0], 2*fold[1]-points[point][xory]] in points):
                listo.append(point)
                print("cheese")
            points[point][xory]=2*fold[1]-points[point][xory]
    for point in listo:
        points.pop(point)
    final = []
    for x in points:
        cheese=0
        for point in final:
            if(point[0]==x[0] and point[1]==x[1]):
                cheese=1
        if(cheese==0):
            final.append(x)
        else:
            print("cheese")
        
    return final

print(len(fold(points, folds[0])))
