"""
Write a python script to calculate average of three numbers entered by user
"""

# taking three number from the user
num1, num2, num3 = int(input("Enter three numbers : ")), int(input()), int(input())

# calculating average
avg = (num1+num2+num3) / 3

# printing average of three numbers
print("Average of", num1, num2, num3, "is", avg)

# print("Average of %d %d and %d is %.2f" %(num1, num2, num3, avg))