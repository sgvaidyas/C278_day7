Numbers = [[1,2,3,4,5,6,7,8,9,10],
          [11,12,13,14,15,16,17,18,19,20]]
Result = []
for list in Numbers:
   Squares = [Number ** 2 for Number in list if Number % 2 == 0]
   Result.extend(Squares)
print(Result)
