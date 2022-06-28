n = int(input("Enter a number"))
for j in range(1,n+1):
    a = [i for i in range(1,j)]
    b = a[::-1]
    print(*a,"  ",*b)
