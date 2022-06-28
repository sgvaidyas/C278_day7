n = int(input("Enter a whole number"))

first_digit = n
last_digit = n
num_digits = 1

while first_digit > 10:
    first_digit = first_digit//10
    num_digits += 1

last_digit = last_digit%10

left_shift = (n-first_digit*10**(num_digits-1))*10+first_digit
right_shift = n//10+last_digit*10**(num_digits-1)

print("left shift: ", left_shift)
print("right shift: ", right_shift)
"""
n=1234

first_digit = 1234
last_digit = 1234
num_digits = 1

----------------------
fd    fd>10  fd//10  num_dig
-------------------------
1234   T      123    1+1=2
123    T      12     2+1=3
12     T      1      3+1=4
1      F-------------------------
===================
num_dig = 4
last_dig = 1234%10 = 4
first_dig = 1
left = (n-first_digit*10**(num_digits-1))*10+first_digit
       (1234-(1*10^3))*10 + 1
       (1234)-1000 *10    + 1
       2340+1=2341

right=n//10+last_digit*10**(num_digits-1)
     =1234//10 + 4*10^3
     =123 +4*1000
     =4123

"""
