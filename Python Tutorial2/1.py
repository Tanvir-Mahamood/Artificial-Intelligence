# print("Hi","Helo world")
# name = "Tanvir"
# age = 23
# price = 25.99
# sts = True
# a = None
# print("My name is", name, "ans I am", age)
# print(type(name))
# print(type(age))
# print(type(price))
# print(type(sts))
# print(type(a))

# a = 2
# b = 3.14
# sum = a + b
# print(sum)

# a, b = 2, 3
# txt = "@"
# print(a*txt*b)

# A = "gmail"
# print((txt+A)*a)

# print(a//b, a/b)

# a = -12
# b = 5
# print(a//b, a/b)
# a, b = b, a 
# print(a//b, a/b)

# # remainder is negative, whan denominator is neative
# a, b = -5, 2
# print(a%b)
# a, b = 5, -2
# print(a%b)

# name = input("name: ")
# age = int(input("age: "))
# age2 = input("age: ")
# price = float(input("enter: "))

# print(type(age))
# print(type(age2))

# deg = "Engineer"
# print(deg+" "+name)
# print(len(deg))

# string indexing does not allow to modify any character
# text = "hello world from python"
# new_text = text[:1] + "a" + text[2:]
# print(new_text)
# print(text[1:4])
# print(text[-3:-1])
# print(text.endswith("ld"))
# print(text.capitalize())
# print(text.replace("python", "c++"))
# print(text.find("x"))
# print(text.find("python"))
# print(text.count("o"))

# text = "hello world From python"
# print(text.upper())
# print(text.lower())

# text2 = "123"
# print(text.isdigit())
# print(text.isalpha())
# text2 = input("enter:")
# print(text2.isdigit())
# print(text2.isalpha())

# validate user input exercise
# 1. username is no more than 12 characters
# 2. username must not contain spaces
# 3. username must not contain digits

username = input("Enter your username: ")

if len(username) > 12:
    print("Your username cannot contain more than 12 characters")
elif not username.find(" ") == -1:
    print("Username cannot hold blank space")
elif not username.isalpha():
    print("username should contain alphanumeric characters")
else:
    print(f"Welcome {username}")


from math import pi
print(pi)
