def game(n):
    nums = [x for x in range(1,n+1)]
    nums = nums[::-1]  #nums[4,3,2,1]
    for i in range(1,n+1):
        if(i % 2 != 0):
            print(i)
            if i < n:
                print(' '.join(str(s) for s in nums))
                nums = nums[1:]

