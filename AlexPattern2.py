def printReverseTree(n):
    numbers = []
    spaces = (n*2)-2
    for i in range(1,n+1):
        numbers.append(i)
        print("".join(str(x) for x in numbers)+(addSpaces(spaces))+"".join(str(x) for x in numbers[::-1]))
        spaces-=2

def addSpaces(x):
    s = ""
    for number in range(int(x)):
        s+= " "
#     print("*", s,"*")
    return s
printReverseTree(4)
