fruits = ["apple", "banana", "cherry"]
numbers = [3, 1.25, 1999, '70']

print("apples" in fruits)  #check membership
print(fruits.count("banana"))   #check membership & number of item
print(fruits.index("cherry"))    #check membership as index position

print(fruits, numbers)

fruits.append("orange") #add new element
print(fruits)

fruits.remove("orange")
print(fruits)

fruits.pop(-1)
print(fruits)

fruits.extend(numbers) #extend with second list, add multiple items
print(fruits)

fruits = ["apple", "banana"]
print(id(fruits))          # 2324988817280

fruits.extend(["cherry"])
print(id(fruits))          # 2324988817280 - id still the same, so = its the same object, just updated

fruits.sort()
print(fruits)