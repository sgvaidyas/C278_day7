import math
num = int(input("Enter your number."))
digits = math.floor(math.log(num, 10))
helper = 10**digits
print("Left shift: ", 10*(num % helper) + num//helper)
print("Right shift: ", helper * (num%10)+ num//10)
"""
num=1234
digits = 3
helper = 10^3 =1000
leftshift = 10*(1234%1000) + 1234//1000 
          = 2340 + 1
          = 2341
rightshift = 1000 * (1234%10) + 1234//10
           = 4000 + 123
           = 4123



"""
