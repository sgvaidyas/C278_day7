def pattern(n):
  nums = list(range(1,n+1)) + list(range(n,0,-1))
  for i in range(1,n+1):
    print(*(x if x<=i else " " for x in nums))

pattern(int(input("n?: ")))
