import math

def degrees_to_radians(degrees):
    return degrees * (math.pi / 180)

degree = 15
radian = degrees_to_radians(degree)
print("Input degree:", degree)
print("Output radian:", round(radian, 6))
