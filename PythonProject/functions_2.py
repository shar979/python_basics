
def add(a, b, c):
    res = a + b+ c
    return res

# when you want to input many numbers ou can
def addition (*nums):
    """

    :param nums:
    :return: integers or floats
    """
    total = sum(nums)
    return total
def build_profile(**kwargs):
    for k, w in kwargs.items():
        print(f"{k}: {w}")


def fancy_functions(name,*nums, **kwargs):
    print(name)
    print(nums)
    print(kwargs)


def my_function(a,b):
    return a/b



   #anonymous ==lambda
   # def square (num):
 #               return num*num
 #    result = square(5)
# print(result)
# square = lambda num : (
# num*num)
# print(square(5))
# result= square(2.9)
# print(result)

surface_area_cylinder = lambda r, h:22 / 7 * r ** 2 *2 +22/7 * 2 * r * h

print(surface_area_cylinder(7,3))

# dictionary for people
people = [
    { "name" : "Alex","age":30},
    {"name" : "Flex","age":70},
    {"name" : "Florida","age":10}
]
# SORTING BY AGE
sorted_by_age = sorted(people, key= lambda x:x["age"])

print(sorted_by_age)

            # build_profile(experience ="100", name="Jane", age=67)
        # calling a function
# print(add(9,7,5))

# print (addition(8,8,6,4,3,2,))