# Author: SMR (AMDG) 09/26/21
radius=int(input("What is the radius of the cylinder?"))
height=int(input("What is the height of the cylinder?"))
surf_area=(2*3.14*radius)*(height+radius)
volume=(3.14)*(radius**2)*(height)
print("The surface area of the cylinder is", surf_area)
print("The volume of the cylinder is", volume)
