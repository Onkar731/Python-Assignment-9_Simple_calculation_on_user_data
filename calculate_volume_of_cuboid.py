"""
Write a python script to calculate volume of a cuboid
"""

# taking length, breadth and height of the cuboid
lenght = float(input("Enter lenght of the cuboid : "))
bredth = float(input("Enter bredth of the cuboid : "))
height = float(input("Enter height of the cuboid : "))

# calculating volume of a cuboid formula - l*b*h
volume = lenght*bredth*height

# printing volume of the cuboid
print("Volume of the cuboid is", volume, "cu.cm")

# print("Volume of the whose length is %.2f, breadth is %.2f and height is %.2f is %.2f cu.cm" %(lenght, bredth, height, volume))