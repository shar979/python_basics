ages = [21,72, 43, 76, 32, 88 ,90, 52]
names=["ian", "Jack", "Moha","Nicky"]

# add an element to the array list
ages.append(31)
# used to delete everything
# ages.clear()
# ages.sort()
# used to reverse
# ages.reverse()

print(ages)
# names.sort()
print(names)

jack_count = names.count("Jack")
print(jack_count)

print(len(names))
print(len(ages))

# how to sum
print(sum(ages)/len(ages))

# to retrieve a specific index
print(ages[0])
print(ages[5])
print(ages[-1])  # printing the last element in the array
print(ages[-2:])
print(names[-10:])
print(ages[3:5])
print(ages[:3]) # to get top three

# set-are used to remove duplicates
scores={88,78,88,65,77,78}
print(scores)
print(max(scores))
print(min(scores))
scores.add(90)
print(scores)
scores.remove(78)
print(scores)

# tuple-immutable
weekdays =("Mon" ,"Tue" ,"Thur", "Frid","Sat", "Sun")
print(weekdays)
print(len(weekdays))
print(weekdays[0])

# dictionary-
person={"name": "Jason", "age":22,"weight":22, "height":1.88}
print(person["name"])
print(person["age"])
print(person["weight"])

people = [{"name":"Aria","age":29},
{"name":"Morris","age":29},
{"name":"Helen","age":56}
]
print(people[0]["age"])
