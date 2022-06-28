from math import *
def rotate(num, shift):
    p = 10 ** shift
    rhs = num // p
    return rhs + (num % p) * 10 ** (floor(log10(rhs)) + 1)

print(rotate(1234,2))
"""

num = 1234
shift = 2

p = 10^2=100
rhs = num//p = 1234//100 = 12
return rhs + (num % p) * 10 ** (floor(log10(rhs)) + 1)
       12  + (1234%100)*10 ^ 2
       12 + 3400 = 3412

"""
