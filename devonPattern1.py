n = 5
for j in range(1,n+1,2):
    print(j)
    if(j<n):
        print(*[i for i in range(n-j//2,0,-1)])
"""
n=5

j :  1 to 6 incrementing 2
======================

j
--------------------
1             1
      1<5 T   5 4 3 2 1
3             3
      3<5 T   4 3 2 1
5             5
	  5<5 F


"""
