n = int(input("Enter a whole number"))

lines = ["".join([str(j+1) for j in range(i)])+" "*2*(n-i)+"".join([str(i-j) for j in range(i)]) for i in range(n+1)]
for line in lines:
    print(line)
"""
for i in range(n+1):
	for j in range(i):
		print(str(j+1))
	for j in range(2*n-i):
	    print(" ")
	for j in range(i):
		print(str(i-j))
  n=4


"""
