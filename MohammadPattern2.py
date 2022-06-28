n=9
for i in range(1,n+1):
    print (*[j+1 for j in range(i)], *["_" for a in range((n*2)-(i*2))], *[b for b in range(i,0,-1)])
