def pattern(num):
    numbers = [i   for i in range(1,num+1)]
    j = 1
    while not j == num+1:
        if (j % 2) == 0:
            print(numbers[::-1])
            numbers.pop()
        elif (j % 2) == 1:
            print(j)
        j += 1

pattern(4)
