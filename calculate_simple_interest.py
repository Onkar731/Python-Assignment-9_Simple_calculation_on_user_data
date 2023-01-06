"""
Write a python script to calculate simple interest
"""

# taking principle amount, rate of interest and time in years
principle_amt = float(input("Enter principle amount : "))
roi = float(input("Enter rate of interest (%) : ")) / 100
time = int(input("Enter time in year : "))

# formula of simple interest - p*r*t
simple_interest = principle_amt*roi*time

# printing simple interest 
print("Simple Interest = ", simple_interest)

# print("Simple Interst = %.2f" %simple_interest)