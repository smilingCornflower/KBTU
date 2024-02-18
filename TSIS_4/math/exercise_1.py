from math import pi

# Write a Python program to convert degree to radian.
# Input degree: 15
# Output radian: 0.261904

def convert_deg_to_rad(degrees):
    return round(degrees * (pi / 180), 6)


angle1, angle2, angle3 = 15, 45, 60

print(f"{angle1} degrees in radians: {convert_deg_to_rad(angle1)}")
print(f"{angle2} degrees in radians: {convert_deg_to_rad(angle2)}")
print(f"{angle3} degrees in radians: {convert_deg_to_rad(angle3)}")


