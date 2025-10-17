# program to calculate the volume of a cylinder.

# Get inputs from user.
radius = float(input("Type radius of the cylinder: "))
height = float(input("Type height of the cylinder: "))

# Constant value of pi
pi = 3.14159

# Calculate volume (v =  πr²h)
volume = pi * (radius ** 2) * height

# Display result with 2 decimal places
print(f"The volume of the cylinder: {volume:.2f}")
