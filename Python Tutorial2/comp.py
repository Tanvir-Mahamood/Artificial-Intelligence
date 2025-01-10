# list comprehension
# [expression for value in iterable if condition]

double = [2 * x for x in range(1, 11)]
print(double)

fruits = ["mango", "banana", "orange", "coconut"]
fruits = [fruit.upper() for fruit in fruits]
fruit_char = [fruit[0] for fruit in fruits]
print(fruits)
print(fruit_char)

numbers = [1, -2, 3, -4, 5, -6]
pos_nums = [val for val in numbers if val >= 0]
print(pos_nums)

