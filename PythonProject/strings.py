f_name= "Juma"
l_name="Joan"
print(f_name.upper())
# only the first letter
full_name=f_name+" "+l_name
print(full_name.title())

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
