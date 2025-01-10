"""
*args = allows you to pass multiple non-key arguments
**kwargs = allows you to pass multiple keyword-arguments
         = * unpacking operator
         1. positional 2. default 3. keyword 4. arbitrary
"""

def add(*args):
    print(type(args))
    total = 0
    for arg in args:
        total += arg
    return total

print(add(1,2,3))

def print_address(**kwargs):
    print(type(kwargs))
    for key, value in kwargs.items():
        print(f"{key} {value}")

print_address(street="12 ab", city = "ddd", state="mi", zip="5400")

def info(*name, **address):
    for word in name:
        print(word, end=" ")
    print()
    for key, value in address.items():
        print(f"{key}, {value}")
    print()
    
    print(address.get("country"))

    if "planet" in address:
        print(address.get("planet"))

info("Eng.", "Tanvir", "Mahamood", home="Rajshahi", country="BD")
info("Doc.", "Tanvir", "Mahamood", home="Rajshahi", country="BD", planet="Earth")