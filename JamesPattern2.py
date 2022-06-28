n = int(input("Enter your number: "))
num_list = [str(i) for i in range(1, n + 1)]
for i in range(1, n + 1):
    print("".join(num_list[:i]) + " "*(n-i)*2 + "".join(num_list[i-1::-1]))
"""
num_list = ["1","2","3","4"]

i= 1     1      1
i=2      12    21
i=3      123  321

"""
