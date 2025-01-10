f_name = "Tanvir"
age = 23
cash = 3.14
print(f"Hello {f_name}, you are {age} years old and your Ac balance is {cash}")

is_student = True
if is_student:
    print("yep")
else:
    print("no")

# typecasting: str(), int(), float(), bool()

cgpa = 3.74
gpa = int(3.74)
print(type(gpa))

# rectangle area calculation
l = float(input("Enter length "))
w = float(input("Enter width: "))
print(f"Area: {l*w}")

# shopping cart
item = input("What item would you like to buy? ")
price = float(input("Enter price: "))
quantity = int(input("Enter quantuity: "))
total = price * quantity
print(f"You have brought {quantity} X {item}")
print(f"Your total: {total}")