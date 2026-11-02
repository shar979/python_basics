import math
from unittest import result
def volume_surface(radius,height):
    v = 22/7 *radius**2 *height
    a= 22/7 *radius**2 *2 +22/7 *radius*2 * height
    return v,a

def greet():
   print("Hello")
# start all functions with define def
def greeting (name):
    print(f"Hello {name}")
    def volume_cylinder(radius, height):
        v = 22 / 7 * radius**2 * height
        print(round(v,2))

 # def volume_cylinder_better(radius,height):
 #            v = 22 / 7 * radius**2 * height
 #           return v


# def volume_cylinder_better(radius, height):

    # pass


# result = volume_cylinder_better(6.5, 8.9)
# print(result)

# with open("volumes.txt", "w")as file:
#     file.write(str(result))

volume, area = volume_surface(10,20)
print(f"{area}")

v,a = volume_surface(radius=10,height=20)
print(f"{v},{a}")

def divide(a, b, should_round=False):
    res = a / b
    if should_round:
        return round(res, 2)
    else:
        return res



print(divide(9,3,False))