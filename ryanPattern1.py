inner_loop = int(input("Enter a number "))
for i in range (1,inner_loop+1):
    for j in range(inner_loop,0,-1):
        if i % 2 != 0:
            print(i,end=" ")
            break
        elif i % 2 == 0:
            print(j, end = " ")
            if j == 1:
                inner_loop -= 1
    print()
