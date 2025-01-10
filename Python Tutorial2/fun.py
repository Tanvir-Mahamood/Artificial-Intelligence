# default argument = it is for certain parameters and used when that argument is omitted

import time 

def net_price(item_price, discount=0, tax=0.05):
    return item_price * (1 - discount) * (1 + tax)

print(net_price(100))
print(net_price(100, 0.1))
print(net_price(100, 0.1, 0.2))

"""
def count(end, start=0):
    for x in range(start, end + 1):
        print(x)
        time.sleep(1)
    print("Done")

count(10)
"""

def hello(gretting, title, fname, lname):
    print(f"{gretting} {title}{fname} {lname}")

hello("Hello", lname="Mahamood", title="Eng.", fname="Tanvir")

print("a", "b", "c", "d", sep="-")

def get_phone(country, area, first, last):
    return f"{country}-{area}-{first}-{last}"

phone_no = get_phone(first=456, last=7890, country=1, area=123)
print(phone_no)