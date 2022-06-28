n =5 # or whatever number
for i in range(n):
    if i % 2 == 0:
        print(i+1)
    else:
        #s=" ".join([str(i) for i in range(int(n-(i-1)/2), 0, -1)])     Can be used instead, but is harder to read
        s=""
        for j in range(n-(i-1)//2, 0, -1):
            s+=str(j) + " "
        print(s)
