import os

# we use print() to dispay an output
print("shar")
print(19)

# declaring a  variable x and printing it to know its type
x=5
print(type(x))

# ways to find square root
import math
y=21
print(math.sqrt(y))

y=21
print(pow(y,2))

# using power and mat at the same time
y=21
print(math.pow(y,2))

# rounding off
y=7.87655
print(round(y,2))

# statements
t=5
if t>0:
    print(t)
else:
    print(t)

    # loops ****
    # loops ****
    r=4
    r=4
    # for x in range(1,r):
        
#         how to insert data into my code
name= input("enter your name:")

age=input("enter your age:")

if not age.isnumeric():
    print("invalid age")
    os._exit(0)
#     to terminate a program use
#     just write os. and click enter it will bring os.exit()
# or you may use sys.exit()

if int(age)>18:
    print(name +" " + "is an adult")
else:
    print(name +" " +"is a child")


