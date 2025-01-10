"""
collection = single "variable" used to store multiple values

List = [] ordered and changable, duplication is allowed. => order matters
Set = {} unordered and immutable, but Add/ Rempve is ok, no duplication
Touple = () ordered and unchangeable, duplication is ok. Faster 
"""

fruits = ["apple", "orange", "mango", "coconut"]
print(fruits[2])
print(fruits[::2])
print(f"index: {fruits.index('orange')}") # if not exists, produce error
print(f"count: {fruits.count('banana')}")
# print(dir(fruits))
# print(help(fruits))
print("apple" in fruits)

fruits[0] = "Apple"
fruits.append("pinapple")
fruits.remove(fruits[0])
fruits.insert(1, "berry")
fruits.sort()
fruits.reverse()
fruits.clear()
for x in fruits:
    print(x, end=" ")