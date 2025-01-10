# num = 5
# parity = "even" if num % 2 == 0 else "odd"
# print("positive" if num > 0 else "negative")
# print(parity)

credit_no = "1234-5678-9012-3456"
print(credit_no[::2])
last_digit = credit_no[-4:]
print(f"XXXX-XXXX-XXXX-{last_digit}")
print(credit_no[::-1])


price1 = 3.14159
price2 = -987.65
price3 = 12.34

print(f"Price1 = ${price1:.2f}")
print(f"Price2 = ${price2:.2f}")
print(f"Price3 = ${price3:.2f}")

print(f"Price1 = ${price1:10}")
print(f"Price2 = ${price2:10}")
print(f"Price3 = ${price3:10}")

print(f"Price1 = ${price1:010}")
print(f"Price2 = ${price2:010}")
print(f"Price3 = ${price3:010}")

print(f"Price1 = ${price1:<10}")
print(f"Price2 = ${price2:<10}")
print(f"Price3 = ${price3:<10}")

print(f"Price1 = ${price1:>10}")
print(f"Price2 = ${price2:>10}")
print(f"Price3 = ${price3:>10}")

print(f"Price1 = ${price1:^10}")
print(f"Price2 = ${price2:^10}")
print(f"Price3 = ${price3:^10}")

print(f"Price1 = ${price1:+}")
print(f"Price2 = ${price2:+}")
print(f"Price3 = ${price3:+}")

print("again")
price1 = 3000.14159
price2 = -9870.65
price3 = 1200.34

print(f"Price1 = ${price1: }")
print(f"Price2 = ${price2: }")
print(f"Price3 = ${price3: }")

print(f"Price1 = ${price1:,}")
print(f"Price2 = ${price2:,}")
print(f"Price3 = ${price3:,}")

print(f"Price1 = ${price1:+,.2f}")
print(f"Price2 = ${price2:+,.2f}")
print(f"Price3 = ${price3:+,.2f}")