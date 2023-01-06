"""
Write a python script to take twonumbers from user (say x and y),
now calculate x power y and display the result
"""

# taking x and y from the user
x, y = int(input("Enter a number and its power to calculate : ")), int(input())

# calculating power using arithmetic exponent operator
power = x**y

# printing power of the number
print(x, "power", y, "is", power)

# print("%d power %d is %d" %(x, y, power))