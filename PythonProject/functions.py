import math

z = math.sqrt (100.5)
print(z)
print(math.pow(5,3))

radius=("20.2")# string
num= float(radius)
print(num-2)

# functions/methods
with open("temp.txt","w") as file:
    file.write("99.34\n")
    file.write("100\n")
    file.write("54.34\n")

with open ("temp.txt","r") as file:
    content = file.read()
    print(content)

    # pip install yt-dlp