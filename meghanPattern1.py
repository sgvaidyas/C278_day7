n = int(input("Enter a whole number"))

num_s = " ".join([str(n-i) for i in range(n)])

for i in range(n):
    if i%2==0:
        print(i+1)
    else:
        print(num_s[i-1:].strip())
