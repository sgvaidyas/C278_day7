n=6
for i in range(1, n+1):
    if i%2 == 0:
        for j in range(n, 0, -1):
            print(j, end = " ")
        n = n-1
    else:
        print(f"\n{i}")


"""
n=6

i --> 1 to 7

i  i%2==0    else
--------------------
1    F        1
2    T
     j= 6 to 0
     			6 5 4 3 2 1
     n=5
3    F         3
4    T
     j=5 to 0
               5 4 3 2 1
     n=4
5    F         5

"""



